import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def Get_voice_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print("Heard from Microphone:" + command)
            command = command.lower()
            if 'microbots' in command:
                command = command.replace("microbots","")
                print(command)
                talk(command)
                return command
    except:
        pass


def run_mainBotLoop():
    command = Get_voice_command()
    print(command)
    if command is None:
        print('Sorry.. try again')

    elif 'exit' in command:
        print("Thank you for using Microbots..")
        talk("Thank you for using Microbots..")
        return(10)

    elif 'play' in command:
        song = command.replace("play","")
        talk("playing " + song)
        print("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is " + time)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

        
    elif 'what is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'who are you' in command:
        talk("I am microbot who is made to serve you till end of my existance")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Sorry dear, I missed that one..')


while True:
    if (run_mainBotLoop() == 10):
        break
    else:
        run_mainBotLoop()
