import speech_recognition

def atr():

    x=speech_recognition.Microphone()
    kayit=speech_recognition.Recognizer()
    with x as voice:
        kayit.adjust_for_ambient_noise(voice)
        sesim = kayit.listen(voice)
        try:
            return kayit.recognize_google(sesim,language="tr-TR")
        except:
            return "Üzgünüm, dediğinizi anlayamadım."
        
def rta():

    x=speech_recognition.Microphone()
    kayit=speech_recognition.Recognizer()
    with x as voice:
        kayit.adjust_for_ambient_noise(voice)
        sesim = kayit.listen(voice)
        try:
            return kayit.recognize_google(sesim,language="en-US")
        except:
            return "Sory, I couldn't understant what you said."
        
if __name__ == "__main__":        
    print("Dinliyorum.")
    a = atr()  
    print(a)