# ------------------------ mikrafon nomi va indexini aniqlash --------------------
import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f'Microphone with name:{name}, index:{index}')

recog = sr.Recognizer()
with sr.Microphone(device_index=5) as source:
    print('Go...')
    audio = recog.listen(source)

query = recog.recognize_google(audio, language='uz-UZ')
print('...' + query.lower())
