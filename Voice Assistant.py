import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import webbrowser
import pyautogui
import time
import cv2
import COVID19Py
import random
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.setProperty('rate',175)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
    #Initialize the recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready...')
        r.pause_threshold = 1
        #wait for a second to let the recognizer adjust the
        #energy threshold based on the surrounding noise level
        #listens for the user's input
        audio = r.listen(source)

    try:
        print("recognizing your voice input.........")
        speak("recognizing your voice input")
        comment=r.recognize_google(audio,language='en-in')
        print(f"I heard u say:{comment}\n")
    except Exception as e:
        print('Your last voice input couldn\'t be heard')
        return "None"
    return comment

def wishing():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("hello sir GoodMorning to you")
    elif time>=12 and time<17:
        speak("hello sir Good Afternoon to you")
    else:
        speak("hello sir Good evening to you ")
    speak("my name is assistant how can i help you")

if __name__=="__main__":
    wishing()
    def Email(text):
        Mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        Mailserver.ehlo()
        Mailserver.starttls()
        Mailserver.login(gmailaddress, password)
        Mailserver.sendmail(gmailaddress, mailto, text)
        Mailserver.close()

    while True:
        comment=myCommand()

        if 'search in Wikipedia' in comment:
            speak("what do you want to seach in wikipedia")
            comment=comment.replace("wikipedia","")
            query=myCommand()
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif'open YouTube'in comment:
            speak("youtube is being opened")
            webbrowser.open("youtube.com")

        elif 'open Google' in comment:
            speak("opening google")
            speak("what do you want to search in google ")
            search=myCommand()
            print(search)
            webbrowser.open('https://google.com/search?q='+search)

        elif 'play music' in comment:
            speak("here you go the music will be played")
            place = 'E:\Virochan folder\songs'
            song = os.listdir(place)
            print(song)
            os.startfile(os.path.join(place, song[0]))

        elif 'time' in comment:
            tm = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {tm}")
            print(tm)

        elif 'open Chrome' in comment:
            speak("chrome application will be opened")
            google = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(google)

        elif 'open eclipse' in comment:
            speak("Eclipse will be opened")
            eclipse="C:/Users/Virochan A C/Desktop/eclipse-java-2020-03-R-win32-x86_64/eclipse/eclipse"
            os.startfile(eclipse)

        elif 'play movie' in comment:
            speak("playing random movie,sit back and enjoy your movie")
            place2 = 'E:\Virochan folder\MOVIES'
            movies = os.listdir(place2)
            print(movies)
            a=random.randint(6,30)
            os.startfile(os.path.join(place2, movies[a]))

        elif 'where is' in comment:
            speak('please tell the place name')
            place=myCommand()
            location="https://www.google.com/maps/place/"+str(place)
            webbrowser.open(location)

        elif 'send email' in comment:
            try:
                speak("Please enter your gmail address sir")
                gmailaddress = input("enter your gmail address")
                print(gmailaddress)
                speak("please enter your gmail password sir")
                password = input("enter your gmail password")
                print(password)
                speak("enter the receiver address")
                mailto=input("enter receivers gmail address")
                print(mailto)
                speak("Tell me what do u want to send through Email")
                text = myCommand()
                Email(text)
                print("Email has been sent successfully")
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                print("sorry could'nt send the mail!!please Try again")
                speak("Sorry Mail has not been sent")


        elif 'hello' in comment:
            speak("hello sir how is your day")
            print("hello sir how is your day")
            str=myCommand()
            if 'great' in str:
                speak("oh that's great,good to hear that")

        elif 'who are you' in comment or 'what is your name' in comment:
            speak("Hey,i am your smart voice assistant coded in python")

        elif  "who created you" in comment:
            speak("I have been created by virochan.")
            print("I have been created by virochan.")

        elif 'take screenshot' in comment:
            im=pyautogui.screenshot()
            im.save('first.png')

        elif "covid-19 details" in comment:
            covid19=COVID19Py.COVID19()
            data=covid19.getAll(timelines=True)
            virusdata=dict(data["latest"])
            names=list(virusdata.keys())
            values=list(virusdata.values())
            print(virusdata)
            time.sleep(2)
            webbrowser.open('https://www.worldometers.info/coronavirus/')

        elif 'open camera' in comment:
            cap=cv2.VideoCapture(0)
            while(True):
                ret, fram=cap.read()
                cv2.imshow("video Capture",fram)
                k=cv2.waitKey(5)
                if(k==27):
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'create folder' in comment:
            try:
                speak('tell the folder name')
                folder=myCommand()
                print(folder)
                where='C:/Users/Virochan A C/Desktop/'
                path=os.path.join(where,folder)
                os.mkdir(path)
            except Exception as e:
                speak('name exist')
                speak('give other name')

        elif 'exit' in comment:
            speak('Exiting....... have a good day')
            print("Exiting.......")
            time.sleep(3)
            sys.exit()