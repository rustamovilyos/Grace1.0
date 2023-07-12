# GRACE
import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
# from num2t4ru import num2text
import webbrowser
import random

tts.oa_speak(f'{config.OA_NAME} sizning xizmatingizda. ..')
# Grace from Peaky Blinders

def oa_respond(voice: str):
    print(voice)
    if voice.startswith(config.OA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.OA_CMD_LIST.keys():
            tts.oa_speak("Buyruq, mandagi buyruqlar qatorida yo'q. ..")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.OA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.OA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.OA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'yordam':
        # help
        text = "Meni turli xil funksiyalarim bor: .."
        text += "vaqtni aniq aytib berish. .."
        text += "turli programmalarni ochish va yopish. .."
        text += "kompyuterni boshqarish. .."
        tts.oa_speak(text)
        # pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Xozir vaqt " + str(now.hour) + " " + str(now.minute)
        tts.oa_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']

        tts.oa_speak(random.choice(jokes))

    elif cmd == 'open_browser':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("http://python.org")


# начать прослушивание команд
stt.oa_listen(oa_respond)
