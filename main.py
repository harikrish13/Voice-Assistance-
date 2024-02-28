import speech_recognition as sr
import pyttsx3                  # python text to speak v3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
from tkinter import *
import os
import random
import smtplib
import cv2
import requests
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
window= Tk()
global var,var1
var=StringVar()
var1=StringVar()

dicts={'india':'in','united states':'us','canada':'ca','australia':'au','new zealand':'nz','united kingdom':'uk'}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_cmd():
        with sr.Microphone() as source:
            print("listening...")
            var.set('Listening...')
            window.update()
            voice = listener.listen(source)
            cmd=''
            try:
                cmd = listener.recognize_google(voice)
                cmd = cmd.lower()
            except sr.UnknownValueError:
                talk('sorry, i did not get that')
                var.set('sorry, i did not get that')
                window.update()
            except sr.RequestError:
                print('sorry, server down')
                var.set('sorry, server down')
                window.update()
        if ('archer' in cmd) or ('' in cmd):
            cmd=cmd.replace('archer','')
            return cmd

def exist(terms):
    for term in terms:
        if term in cmd:
            return True

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk('good morning sir')
        var.set('good morning sir')
        window.update()
    elif hour>=12 and hour<18:
        talk('good afternoon sir')
        var.set('good afternoon sir')
        window.update()
    else:
        talk('good evening sir')
        var.set('good evening sir')
        window.update()

    talk("how can i help you")
    var.set("how can i help you")
    window.update()

def run_iris():
    global cmd
    cmd = take_cmd()

    if exist(['bye','shutdown','quit','tata','see you soon']):
        talk("ok bye sir, see you soon")
        var.set("ok bye sir, see you soon")
        window.update()
        exit()

    elif exist(['morning','afternoon','evening','night']):
        wish()

    elif 'mail' in cmd:
        se='hari262002@gmail.com'
        talk('whom do you want to send the mail!!!')
        re=take_cmd()
        s=re.split(' ')
        re1=''
        for i in s:
            re1+=i
        pasw='poporatratnew'
        talk('what message you want me to deliver')
        mssg=take_cmd()
        sev=smtplib.SMTP('smtp.gmail.com', 587)
        sev.starttls()
        sev.login(se,pasw)
        talk('login successful')
        var.set('login successful')
        sev.sendmail(se,re1,mssg)
        talk('mail sent successful')
        var.set('mail sent successful')

    elif ('play' in cmd) or ('song' in cmd):
        if exist(['play me a song','play a song']):
            talk('sure')
            talk('what song you would like to hear...')
            song=take_cmd()
            song = song.replace('song', '')
            var.set('playing'+song)
            window.update()
            talk('playing'+song)
            pywhatkit.playonyt(song)
        else:
            talk('sure')
            song = cmd.replace('song', '')
            song = song.replace('play', '')
            song = song.replace('please', '')
            song=song.replace('can you','')
            var.set('playing' + song)
            window.update()
            talk('playing' + song)
            pywhatkit.playonyt(song)

    elif exist(['hi','hello','hey','hai']) and ('say' not in cmd):
        g=["hi sir, how can I help you", "hey sir, what's up?", "hey sir, how can I help you?", "hello sir, how may i help you"]
        r=random.randint(0,3)
        grt=g[r]
        var.set(grt)
        window.update()
        talk(grt)

    elif 'what can you do' in cmd:
        talk('i can do things which can stun you!!!')
        talk('''like
        playing songs
        opening applications
        surfing on google
        searching on wikipedia
        writing an email
        taking notes
        updating with latest news across countries
        and so on....''')
        var.set('''like
        playing songs
        opening applications
        surfing on google
        searching on wikipedia
        writing an email
        taking notes
        updating with latest news across countries
        and so on....''')
        window.update()

    elif 'thank you' in cmd:
        talk('you are welcome')
        var.set('you are welcome')
        window.update()

    elif 'your name' in cmd:
        var.set('I am Archer, your personal assistant')
        window.update()
        talk('i am archer, your personal assistant')

    elif 'time' in cmd:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is '+time)
        var.set('Current time is '+time)
        window.update()

    elif 'say hello' in cmd:
        var.set('hello everyone!, myself archer')
        window.update()
        talk('hello everyone!, myself archer')

    elif exist(['wikipedia','wiki']):
        talk('looking in wikipedia')
        person = cmd.replace(' wikipedia', '')
        person = person.replace('who is ', '')
        turl = "https://en.wikipedia.org/wiki/"+person
        webbrowser.get().open(turl)
        text = wikipedia.summary(person, 1)
        talk('this is what i found')
        var.set(text)
        window.update()
        talk(text)

    elif 'joke' in cmd:
        jk=pyjokes.get_joke()
        var.set(jk)
        window.update()
        talk(jk)

    elif exist(['diary','notes','entry']):
        if 'diary' in cmd:
            talk('what is your title')
            title=take_cmd()
            f=open(title+'.txt','wt')
            talk('go ahead start talking for your diary entry')
            t=take_cmd()
            if 'save and close the file' in t:
                t = t.replace(' save and close the file', '')
                f.write(t)
                f.close()
                talk('file successfully saved')
        elif 'notes' in cmd:
            talk('what is your title')
            title = take_cmd()
            f = open(title + '.txt', 'wt')
            talk('go ahead start talking for your notes')
            t = take_cmd()
            if 'save and close the file' in t:
                t=t.replace(' save and close the file','')
                f.write(t)
                f.close()
                talk('file successfully saved')
        elif 'entry' in cmd:
            talk('what is your title')
            title = take_cmd()
            f = open(title + '.txt', 'wt')
            talk('go ahead start talking for your entry')
            t = take_cmd()
            if 'save and close the file' in t:
                t = t.replace(' save and close the file', '')
                f.write(t)
                f.close()
                talk('file successfully saved')

    elif 'open' in cmd:
        app = cmd.replace('open ', '')
        if 'vlc' in app:
            var.set("opening VLC media Player")
            window.update()
            talk("opening V L C media player")
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(path)

        elif 'pycharm' in app:
            var.set("opening pycharm")
            window.update()
            talk("opening pycharm")
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'calculator' in cmd:
            var.set("opening calculator")
            window.update()
            talk("opening calculator")
            os.startfile('calc.exe')

        elif 'soptify' in cmd:
            var.set("opening Spotify")
            window.update()
            talk("opening Spotify")
            os.startfile('spotify.exe')

        elif 'google' in cmd:
            turl = "http://google.com/search?q="
            var.set('opening google')
            window.update()
            talk('opening google')
            webbrowser.get().open(turl)

        elif 'notepad' in cmd:
            var.set('opening notepad')
            window.update()
            talk('opening notepad')
            os.startfile('notepad.exe')

        elif 'camera' in cmd:
            var.set('opening camera')
            window.update()
            talk('opening camera')
            cam=cv2.VideoCapture(0)
            frame = 30
            talk('to take picture click c')
            while cam.isOpened():
                ret,img=cam.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(2) == ord('c'):
                    break
            def get_image():
                ret,img = cam.read()
                return img
            for i in range(frame):
                temp = get_image()
            talk('say cheese...')
            cam_cap = get_image()
            talk('say file name to save..')
            f=take_cmd()
            file = f+'.png'
            cv2.imwrite(file, cam_cap)
            cv2.destroyAllWindows()
            talk('picture taken...')

    elif ('news' in cmd) or ('headlines' in cmd):
        talk('which country news you want')
        n=take_cmd()
        k=dicts.keys()
        if n in k:
                v=dicts.get(n)
                r = requests.get('http://newsapi.org/v2/top-headlines?country='+v+'&apiKey=09d9c79ff38f4fb79fa5cf6486ac6648')
                data = json.loads(r.content)
                var.set('here are some top 10 headlines of today')
                window.update()
                talk('here are some top 10 headlines of today')
                for j in range(10):
                    news = data['articles'][j]['title']
                    var.set(news)
                    talk('headline'+str(j+1))
                    var.set(news)
                    window.update()
                    talk(news)
                var.set("that's all for today's news")
                window.update()
                talk('thats all for todays news')

        else:
            talk('news are only available for india, united states, australia, united kingdom, new zealand, canada')
            talk('try again')

    elif ('search' in cmd) or ('google' in cmd):
        cmd = cmd.replace('search','')
        cmd = cmd.replace('google','')
        turl = "http://google.com/search?q="+cmd
        webbrowser.get().open(turl)
        var.set("here are few results")
        window.update()
        talk("here are few results")
    elif exist(['who','how','what','when','where']):
        turl = "http://google.com/search?q=" + cmd
        webbrowser.get().open(turl)
        var.set("here are few results")
        window.update()
        talk("here are few results")
    else:
        talk("I'm sorry, but I can't help with that.")
        talk(" I'm still learning")
        uf=open('suggestion.txt','at')
        uf.write(cmd)
        talk('your command is noted...')
        uf.close()

def update(ind):
    frame = frames[(ind)%100]
    ind+=1
    label.configure(image=frame)
    window.after(100, update, ind)

label1 = Label(window, textvariable = var1, bg = '#FAB60C')
label1.config(font=("Courier", 20))
var1.set('ARCHER')
label1.pack()
label2 = Label(window, textvariable = var, bg = '#ADD8E6')
label2.config(font=("Courier", 10))
var.set('')
label2.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('ARCHER')

label = Label(window,width = '1900', height = '650')
label.pack()
window.after(0, update, 0)

ph=PhotoImage(file='voice.png')
btn3=Button(window,image=ph,command= run_iris)
btn3.pack()

btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()


