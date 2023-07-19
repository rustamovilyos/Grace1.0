# GRACE
import os
import subprocess

import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
# from num2t4ru import num2text
import webbrowser
import random

from functions.soat import num2words, eng2uzb

tts.oa_speak(f'{config.OA_NAME} sizning xizmatingizda. ..')


# Grace from Peaky Blinders
# oa - ovozli assistent
def oa_respond(voice: str):
    print("You said: ", voice)
    if voice.startswith(config.OA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.OA_CMD_LIST.keys():
            tts.oa_speak("Buyruq, mendagi buyruqlar ro'yxatida yo'q. ..")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    # print("raw voice: ", raw_voice)
    cmd = raw_voice

    for x in config.OA_ALIAS:
        # print("x alias: ", x)
        cmd = cmd.replace(x, "").strip()
        # print("cmd alias: ", cmd)

    for x in config.OA_TBR:
        # print("x tbr: ", x)
        cmd = cmd.replace(x, "").strip()
        # print("cmd tbr: ", cmd)

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    # print("rc: ", rc)
    for c, v in config.OA_CMD_LIST.items():
        # print(f"c: {c}, v: {v}")

        for x in v:
            vrt = fuzz.token_set_ratio(cmd, x)
            # print("vrt: ", vrt)
            if vrt > rc['percent']:
                # print("rc percent: ", rc["percent"])
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'info':
        # info
        text = "Meni turli xil funksiyalarim bor: .."
        text += "vaqtni aniq aytib berish. .."
        text += "turli programmalarni ochish va yopish. .."
        text += "kompyuterni boshqarish. .."
        tts.oa_speak(text)
    elif cmd == 'ctime':
        # current time
        hour = eng2uzb(num2words(datetime.datetime.now().strftime("%H")))
        minute = eng2uzb(num2words(datetime.datetime.now().strftime("%M")))
        text = "Xozir vaqt " + str(hour) + "-u, " + str(minute) + ". .."
        tts.oa_speak(text)

    elif cmd == 'terminal':
        tts.oa_speak("terminalni ochyapman... ..")
        exec(open("functions/terminal.py").read())

    elif cmd == 'open_browser':
        tts.oa_speak("brazerni ochyapman... ..")
        exec(open("functions/chrome.py").read())


# начать прослушивание команд
stt.oa_listen(oa_respond)
