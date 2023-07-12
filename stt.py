import json

import vosk
import sys
import sounddevice as sd
import queue

model = vosk.Model('model')
samplerate = 16000
device = 5

q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)

    q.put(bytes(indata))


def oa_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])
                # print(rec.Result())

