import torch
import sounddevice as sd
import time

language = 'uz'
model_id = 'v3_uz'
device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)  # gpu or cpu

example_text = "Salom, Ilyos. Men, Silero, kutubxonasining matnlarni o'zbekcha, qiz bolaning ovozi bilan o'qib " \
               "beruvchi modeliman. Ushbu model turli xil tillarni o'z ichiga oladi. .."


def oa_speak(what: str):
    sample_rate = 48000
    speaker = 'dilnavoz'
    put_accent = True
    put_yo = True
    # example_text = 'Labbay.'
    audio = model.apply_tts(text=what,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    print(what)
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()


# oa_speak(example_text)
