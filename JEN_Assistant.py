''' Importing all Required Modules and Libraries'''
import pyttsx3 # pip install pyttsx3
import datetime # pip install datetime
import wikipedia # pip install wikipedia
import os
import random
import cv2 # pip install opencv
import webbrowser
import statistics
import calendar
import smtplib #pip install smtplib
import tqdm # pip install tqdm or TQDM
import time
import turtle
import math
import subprocess
import PIL # pip install pillow
import phonenumbers # pip install phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from twilio.rest import Client # pip install twilio
from tkinter import *  # pip install tkinter
from tkinter import ttk,colorchooser,filedialog
from PIL import ImageGrab

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
master=''

# Making a Speak Function so that the assistant can speak
def speak(audio):
    '''Taking String as Input. Audio is the Output'''
    engine.say(audio)
    engine.runAndWait()


# The Load function is made for showing the progressbar or start up of the assistant
def load():
    '''Shows the Progress Bar'''
    speak("Initializing JEN")
    print("Initializing J.E.N")
    speak("Loading All Drivers...")
    print("Loading All Drivers...") 
    for i in tqdm.trange(100):
        time.sleep(0.1) 


# The assistant introduces itself
def assistant():
    '''The assistant introduces itself and tells what all it can do'''
    speak("I am Jen;your assistant")
    t=("date;","Day;","time;","birthday;","information;")
    t1=("Play music;","chat;","Open Camera","Open Google","do Math","send SMS's","and E Mails")
    speak("I can Do many things like")
    speak('Telling you')
    speak(t)
    speak("I can Also")
    speak(t1)


#  the Day Function tells the day e.g Monday, Tuesday
def day():
    '''Using in-buildt calendar module to check for the day no input needed '''
    monday=calendar.MONDAY
    tuesday=calendar.TUESDAY
    wednesday=calendar.WEDNESDAY
    thursday=calendar.THURSDAY
    friday=calendar.FRIDAY
    saturday=calendar.SATURDAY
    sunday=calendar.SUNDAY
    today=datetime.date.today()
    if today.weekday()==monday:
        speak("Today is Monday")
    elif today.weekday()==tuesday:
        speak("Today is Tuesday")
    elif today.weekday()==wednesday:
        speak("Today is Wednesday")
    elif today.weekday()==thursday:
        speak("Today is Thursday")
    elif today.weekday()==friday:
        speak("Today is Friday")
    elif today.weekday()==saturday:
        speak("Today is Saturday")
    elif today.weekday()==sunday:
        speak("Today is Sunday")
    else:
        speak("Sorry!!")


# Sends sms to the users phone (needs twolio account)  
def sms(b):
    account_sid = 'AC9e134fec17393918a5f4ded6fb8978fe'
    auth_token = '533bb95874f62b05f6ce2996354b31c0'
    client =Client(account_sid, auth_token)
    message= client.messages \
                    .create(
                            body=b,
                            from_='+19095808853',
                            
                            to="+919620907708"
                            )
    speak("message Successfully Sent!!")


# Performs Mathamatical Calculations
def calculation(num1,num2,op):
    if op=="+":
        add=num1+num2
        speak(add)
        speak('is the answer')
        print(add)
    elif op=="-":
        sub=num1-num2
        speak(sub)
        speak('is the answer')
        print(sub)
    elif op=="/":
        div=num1/num2
        speak(div)
        speak(str(div)+'is the answer')
        print(div)
    elif op=='*':
        mul=num1*num2
        speak(mul)
        speak('is the answer')
        print(mul)
    elif op=='//':
        fdiv=num1//num2
        speak(fdiv)
        speak('is the answer')
    elif op=='**':
        p=math.pow(num1,num2)
        speak(p)
        speak('is the answer')
    else:
        speak('Sorry i don\'t calculate with this operation')


# Performs Statistical calculations like Mean Median and Mode 
def do_statistics(values,statask):
        v=list(map(float,values.split(',')))
        if statask=="Mean" or statask=="MEAN" or statask=="mean":
            speak('Mean is'+str(statistics.mean(v)))
            print(statistics.mean(v))
        elif statask=="Median" or statask=="MEDIAN" or statask=="median":
            speak('Median is'+str(statistics.median(v)))
            print(statistics.median(v))
        elif statask=="Mode" or statask=="MODE" or statask=="mode":
            speak('Mode is'+str(statistics.mode(v)))
            print(statistics.mode(v))
        else:
            speak("Mean is ")
            speak(statistics.mean(v))
            speak("Median is ")
            speak(statistics.median(v))
            print("Median is =",statistics.median(v))
            speak("Mode is")
            speak(statistics.mode(v))
            print("Mode is =",statistics.median(v))


# Chats with the user with hard quoted inputs and responses
def chat(text):
    if 'hey' in text.lower():
        speak('Hi How are you')
    elif 'who are you' in text:
        speak('i am Jen your assistant')
    elif 'family' in text.lower():
        speak('i consider everyone to be my family')
    elif 'you live' in text.lower():
        speak('i live in the cloud,i\'m here whenever you want to chat') 
    elif 'your face' in text.lower():
        speak('i\'m as beautiful as you')
    elif 'love me' in text.lower():
        speak('Without you,i have no purpose')
    elif 'miss you' in text.lower():
        speak('not to worry,i\'m right here')   


#  Sends email to the email id provided
def send_email(emailid,msg):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('imalphai70@gmail.com','AI_ALPHA123!')
        server.sendmail('imalphai70@gmail.com',email_id,msg)
        send_email(emailid,msg)
        speak("Mail Successfully Sent!!")
        print("Mail Successfully Sent!!")


# Opens Google Maps in the Browser 
def map_():
    webbrowser.open('https://www.google.co.in/maps?hl=en&tab=kl&authuser=1')  


# Opens the Systems Camera (Webcam)
def camera():
        capture=cv2.VideoCapture(0)
        while True:
            ret,frame=capture.read()
            cv2.imshow('Camera',frame)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()


# Opens a special app for Drawing
def draw():
    class main:
        def __init__(self,master):
            self.master=master
            self.color_fg='black'
            self.color_bg='white'
            self.old_x=None
            self.old_y=None
            self.penwidth=5
            self.drawWidget()
            self.c.bind('<B1-Motion>',self.paint)
            self.c.bind('<ButtonRelease-1>',self.reset)
        def paint(self,e):
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)
            self.old_x=e.x
            self.old_y=e.y
        def  reset(self,e):
            self.old_x=None
            self.old_y=None

        def changeW(self,e):
            self.penwidth=e

        def save(self):
            file=filedialog.asksaveasfilename(filetype=[('Portable Network Graphics','*.png')])
            if file:
                x=self.master.winfo_rootx()+self.c.winfo_x()
                y=self.master.winfo_rooty()+self.c.winfo_y()
                x1=x+self.c.winfo_rootx()+self.c.winfo_width()
                y1=y+self.c.winfo_rooty()+self.c.winfo_heigth()

                PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file+'.png')
        def clear(self):
            self.c.delete(ALL)
        def change_fg(self):
            self.color_fg=colorchooser.askcolor(self.color_fg)[1]
            self.c['bg']=self.color_bg
        def change_bg(self):
            self.color_bg=colorchooser.askcolor(self.color_bg)[1]
            self.c['bg']=self.color_bg


        def drawWidget(self):
            self.controls=Frame(self.master,padx=5,pady=5)
            Label(self.controls,text='Pen Width :',font=('',15)).grid(row=0,column=0)
            self.slider=ttk.Scale(self.controls,from_=5,to=100,command=self.changeW,orient=HORIZONTAL)
            self.slider.set(self.penwidth)
            self.slider.grid(row=0,column=1,ipadx=30)
            self.controls.pack()

            self.c=Canvas(self.master,width=500,height=400,bg=self.color_bg,)
            self.c.pack(fill=BOTH,expand=True)

            menu=Menu(self.master)
            self.master.config(menu=menu)
            filemenu=Menu(menu)
            menu.add_cascade(label='File',menu=filemenu)
            filemenu.add_command(label='Export',command=self.save)
            colormenu=Menu(menu)
            menu.add_cascade(label='Colour',menu=colormenu)
            colormenu.add_command(label='Brush Colour',command=self.change_fg)
            colormenu.add_command(label='Background Colour',command=self.change_bg)
            optionmenu=Menu(menu)
            menu.add_cascade(label='Options',menu=optionmenu)
            optionmenu.add_command(label='Clear Canvas',command=self.clear)
            optionmenu.add_command(label='Exit',command=self.master.destroy)
        
    root=Tk()
    main(root)
    root.title('Drawing Board')
    root.mainloop()


#  Opens the snake game which is made using turtle
def game():
    delay=0.1
    score=0
    high_score=0
    life=3
    #making screen
    wn=turtle.Screen()
    wn.title('Snake Game')
    wn.bgcolor('black')
    wn.setup(width=600,height=600)
    wn.tracer(0)
    #snake head
    head=turtle.Turtle()
    head.speed(0)
    head.shape('square')
    head.color('green')
    head.penup()
    head.goto(0,0)
    head.direction='stop'
    #Snake Body
    segment=[]
    #snake food
    food=turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color('red')
    food.penup()
    food.goto(0,100)
    #Pen
    pen=turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('yellow')
    pen.penup()
    pen.hideturtle()
    pen.goto(0,275)
    pen.write("Score: 0  High Score: 0  Life:3",align='center',font=('Courier',11,'normal'))
    #Function
    def go_up():
        if head.direction!='down':
            head.direction='up'
    def go_down():
        if head.direction!='up':
            head.direction='down'
    def go_left():
        if head.direction!='right':
            head.direction='left'
    def go_right():
        if head.direction!='left':
            head.direction='right'  
    def move():
        if head.direction=='up':
            y=head.ycor()
            head.sety(y+20)
        if head.direction=='down':
            y=head.ycor()
            head.sety(y-20)
        if head.direction=='left':
            x=head.xcor()
            head.setx(x-20)
        if head.direction=='right':
            x=head.xcor()
            head.setx(x+20)
    #keyboard binding
    wn.listen()
    turtle.onkeypress(go_up,'Up')
    turtle.onkeypress(go_down,'Down')
    turtle.onkeypress(go_left,'Left')
    turtle.onkeypress(go_right,'Right')
    #main game loop
    while True:
        wn.update()
        #checking for border collision
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            #hiding segments
            for s in segment:
                s.goto(1000,1000)
            #clearing segments
            segment.clear()
            #Reseting the score
            score=0
            life-=1
            pen.clear()
            pen.write("Score:{}  High Score:{}  Life:{}".format(score,high_score,life),align='center',font=('Courier',11,'normal'))
            #Reset delay
            delay=0.1
        #Checking for food collision
        if head.distance(food)<20:
            mof_x=random.randint(-288,288)
            mof_y=random.randint(-288,288)
            food.goto(mof_x,mof_y)
            #adding body
            new_segment=turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape('square')
            new_segment.color('green')
            new_segment.penup()
            segment.append(new_segment)
            #Shortening the delay
            delay-=0.001
            #Increasing the score
            score+=10
            if score>high_score:
                high_score=score
            pen.clear()
            pen.write("Score:{}  High Score:{}  Life:{}".format(score,high_score,life),align='center',font=('Courier',11,'normal'))
        #move the end segment
        for i in range(len(segment)-1,0,-1):
            x=segment[i-1].xcor()
            y=segment[i-1].ycor()
            segment[i].goto(x,y)
        #segment 0 movement 
        if len(segment)>0:
            x=head.xcor()
            y=head.ycor()
            segment[0].goto(x,y)

        move()
        #check for head and body collision
        for s in segment:
            if s.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction='stop'
                #hiding segments
                for s in segment:
                    s.goto(1000,1000)
                #clearing segments
                segment.clear()
                #reseting the score
                score=0
                life-=1
                #updating the score
                pen.clear()
                pen.write("Score:{}  High Score:{}  Life:{}".format(score,high_score,life),align='center',font=('Courier',11,'normal'))
                #Reset delay
                delay=0.1
        if life==0:
            pen.color('blue')
            pen.goto(0,0)
            pen.write("You Lose!! Try Again!!",align='center',font=('Courier',24,'normal'))
            time.sleep(1.5)
            break

        
        time.sleep(delay)


# Searches for the number provided in the database of phonenumbers
def find_phone(no):
    number=phonenumbers.parse(no)
    location='Location of this Phone Number is :' + geocoder.description_for_number(number,'en')
    company='The Phone Number is of'+carrier.name_for_number(number,'en') +'Company'
    
    speak(location)
    print('Location of this Phone Number is :',geocoder.description_for_number(number,'en'))
    speak(company)
    print('The Phone Number is of',carrier.name_for_number(number,'en'),'Company',sep=' ')
    return location,company


#  Restarts the Computer
def restart():
    speak('Do you want to restart')
    restart_ask=input('Please Enter[Y/N]:')
    if 'y' or 'Y' in restart_ask:
        os.system('restart /r /t 00')
    else:
        speak('the computer won\'t restart')


#  Shuts Down the Computer
def shutdown():
    speak("Are you Sure?")
    choice=input("Please Enter [Y or N]: ")
    if choice=="y" or choice=="Y":
        os.system("shutdown /s /t 00")
    else:
        speak("The Computer Won't Shutdown!")  


# Writes into a text file automatically
def auto_write(wat_2_write):
    f=open('E:\\Write.txt','w')
    lines=[]
    lines.append(wat_2_write)
    f.writelines(lines)
    os.startfile('E:\\Write.txt')


# Opens Notepad for you to write
def self_write():   
    subprocess.Popen(['notepad.exe'])       


# Tells you today's Date
def date():
    speak("Today's Date is")
    speak(datetime.date.today())


#  Tells you the current time
def time_():
    now = datetime.datetime.now()
    ct=now.strftime("%H:%M")
    speak("Right Now the Time is")
    speak(ct)


# Webscrapes Wikipedia with its API and gives the information about it
def information(infoabt):
    info=wikipedia.summary(infoabt,sentences=3)
    speak("According to WIKIPEDIA..")
    print(info)
    speak(info)
    return info


# Plays Music from the directory you provided
def play_music(music_dir):
    songs=os.listdir(music_dir)
    rand=random.randrange(len(songs))
    os.startfile(os.path.join(music_dir,songs[rand]))
    speak("song has started")


# Opens Google in the Browser
def open_google():
    webbrowser.open_new_tab(url='google.co.in')


# Activates command mode and talks to you formally
def command():
    speak("JEN is ready for your command!!!")


#  Wishes you According to the time
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")   


# Opens CMD 
def open_cmd():
    subprocess.Popen(['cmd.exe'])


def open_powershell():
    subprocess.Popen(['powershell.exe'])


#  Sets times for the no. of seconds provided by the user
def timer_(s):
    try:
        when_to_stop=abs(int(s))
    
    except Exception:
        print('Not a Number')
        
    
    while when_to_stop>0:
        m,s=divmod(when_to_stop,60)
        h,m=divmod(m,60)
        timer=str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2)
        time.sleep(1)
        print(timer+'\r',end='')
        when_to_stop-=1
    speak('Times Up')


