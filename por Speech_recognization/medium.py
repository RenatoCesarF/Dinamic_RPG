import speech_recognition as sr
import pyaudio
from playsound import playsound


def ouvir_microfone():

    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        audio = microfone.listen(source)
    try:
        frase = ''
        frase = microfone.recognize_google(audio, language='pt-BR').lower()

        #------função que corta a frase-------#
        filter = frase.split()
    
        #Caso nada seja dito, retorna
        if filter == []:
            return

        #Caso algo seja dito, reproduz (beta)    
        else:

            #-------função que reproduz audio--------#
            print(filter)
            if ('flecha' or 'flash') in filter:
                playsound('Sounds/Arrow/arrow_disp.mp3')
            if ('fogo' and 'bola') in filter:
                playsound('Sounds/Spells/fireBall.mp3')
            
        
    except sr.UnknownValueError:
        return


    
while True:
    ouvir_microfone()


