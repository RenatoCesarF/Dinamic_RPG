import speech_recognition as sr
import pyaudio

from playsound import playsound


def ouvir_microfone():

    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)
    try:
        frase = ''
        frase = microfone.recognize_google(audio, language='pt-BR')

        #------função que corta a frase-------#
        filter = frase.split()
    
        #Caso nada seja dito, retorna
        if filter == []:
            return

        #Caso algo seja dito, reproduz (beta)    
        else:

            #-------função que reproduz audio--------#
            print(filter)
            if 'flecha' in filter:
                playsound('Sounds/Arrow/arrow_disp.mp3')

        
    except sr.UnknownValueError:
        return


    
while True:
    ouvir_microfone()

