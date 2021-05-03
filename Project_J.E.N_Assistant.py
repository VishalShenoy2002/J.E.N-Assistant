from JEN_AI.JEN_Assistant import * # Self - Made Module
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askdirectory

# Setting Default Colours for the Interface
backgroundcolor='purple4'
framecolor='purple3'
buttoncolor='maroon1'

# Creating the Mainscreen

# Note :-
#     Using .pack() and .place() to arrage the widgit in the window
class MainScreen:
    def __init__(self,master):
        
    #========== W I N D O W ==========#

        # Making the Window
        self.master=master # Making a Callable Master Variable
        self.master.geometry('600x600') # Setting the Screen Size (widthxheight)
        self.master.resizable(0,0)  # Not allowing the User to Resize
        self.master.title('J.E.N Assistant') # Giving the Title for the Screen (in titlebar)
        self.master.configure(bg=backgroundcolor) # Setting the background color

    #========== H E A D I N G  &   F R A M E ==========#

        # Making the Heading
        self.heading=Label(self.master,text='J.E.N Assistant',font=('Rockwell',30,'bold')) # Creating a Label which will be inside the window(Heading indide the screen)
        self.heading.configure(bg=backgroundcolor) # Setting background color 
        self.heading.pack() # Placing the  heading inside the window

        # Making the Frame which comes in the Window
        self.frame=Frame(self.master,height=520,width=520,bd=15,relief=GROOVE)
        self.frame.configure(bg=framecolor) # Setting the background color for the Frame
        self.frame.pack() # Placing the Frame inside the window

    # ========== B U T T O N S ==========#

        # Creating a Start Button with a start function 

        self.start_button=Button(self.frame,text='START',font=('',15,'bold'),width=25,command=self.start) # Making the Button for Starting the Assistant
        self.start_button.configure(bg=buttoncolor) # Setting the background color for the Button 
        self.start_button.place(x=100,y=100) # Placing the Buttons inside the Frame

        # Creating a Change Skin Button with a change_skin function 

        self.change_skin_button=Button(self.frame,text='CHANGE SKIN',font=('',15,'bold'),width=25,command=self.change_skin) # Making the Button for Changing the theme of the assistant
        self.change_skin_button.configure(bg=buttoncolor) # Setting the background color for the Button
        self.change_skin_button.place(x=100,y=200) # Placing the Buttons inside the Frame

        # Using .mainloop() to keep the window open

        self.master.mainloop()



    # Defining the start(self) for the start_button for opening a New Screen

    def start(self): 
        wishme()
        command()
        self.Screen=Toplevel(self.master) # Creating a Toplevel window or a sub-screen
        self.app=CommandScreen(self.Screen) # Opening the Sub-screen


    # Sefining the change_skin(self) for change skin button for changing the theme of the assistant
    def change_skin(self):
        # Making a integer variable so that it changes theme accoring to the value
        Skin_Val=IntVar() 
        
        
        def change(): 
            # Checking if the Value is 1 
            if Skin_Val.get()==1: 
                global backgroundcolor # Calling 
                global framecolor  # Calling the Global framecolor
                global buttoncolor # Calling the Global buttoncolor 

                backgroundcolor='dark green' # Changing the Colors to green
                framecolor='sea green' # Changing the Colors to green
                buttoncolor='lime green' # Changing the Colors to green

                self.master.configure(bg=backgroundcolor) # Setting the Beckground Color to dark green
                self.heading.configure(bg=backgroundcolor) # Setting the Beckground Color to dark green

                self.frame.configure(bg=framecolor) # Setting  the Frame Color to sea green
                self.blue_button.configure(bg=framecolor) # Setting  the Frame Color to sea green
                self.green_button.configure(bg=framecolor) # Setting  the Frame Color to sea green
                self.default_button.configure(bg=framecolor) # Setting  the Frame Color to sea green

                self.start_button.configure(bg=buttoncolor) # Setting the Button Color to lime green
                self.change_skin_button.configure(bg=buttoncolor) # Setting the Button Color to lime green
                self.change_skin.configure(bg=buttoncolor) # Setting the Button Color to lime green
                

            elif Skin_Val.get()==2: # Checking if the Value is 2
                backgroundcolor='midnight blue' # Changing the color to blue
                framecolor='medium blue' # Changing the color to blue
                buttoncolor='deep sky blue' # Changing the color to blue

                self.master.configure(bg=backgroundcolor) # Setting the background Color to midnight Blue
                self.heading.configure(bg=backgroundcolor) # Setting the background Color to midnight Blue

                self.frame.configure(bg=framecolor) # Setting the Frame Color to  medium Blue
                self.blue_button.configure(bg=framecolor) # Setting the Frame Color to  medium Blue
                self.green_button.configure(bg=framecolor) # Setting the Frame Color to  medium Blue
                self.default_button.configure(bg=framecolor) # Setting the Frame Color to  medium Blue

                self.start_button.configure(bg=buttoncolor) # Setting the BUtton Color to deep sky Blue
                self.change_skin_button.configure(bg=buttoncolor) # Setting the BUtton Color to deep sky Blue
                self.change_skin.configure(bg=buttoncolor) # Setting the BUtton Color to deep sky Blue
                
            else: # Checking if the Value is 3

                backgroundcolor='purple4' # Changing the color to purple (Default)
                framecolor='purple3' # Changing the color to purple (Default)
                buttoncolor='maroon1' # Changing the color to purple (Default)

                self.master.configure(bg=backgroundcolor) # Setting the Background color to Default color i.e. Purple4
                self.heading.configure(bg=backgroundcolor) # Setting the Background color to Default color i.e. Purple4

                self.frame.configure(bg=framecolor) # Setting the Frame color to Default color i.e. Purple3
                self.blue_button.configure(bg=framecolor) # Setting the Frame color to Default color i.e. Purple3
                self.green_button.configure(bg=framecolor) # Setting the Frame color to Default color i.e. Purple3
                self.default_button.configure(bg=framecolor) # Setting the Frame color to Default color i.e. Purple3
                
                self.start_button.configure(bg=buttoncolor) # Setting the Button color to Default color i.e. Maroon1
                self.change_skin_button.configure(bg=buttoncolor) # Setting the Button color to Default color i.e. Maroon1
                self.change_skin.configure(bg=buttoncolor) # Setting the Button color to Default color i.e. Maroon1
                
 
        self.green_button=Radiobutton(self.frame,text='Green Skin',value=1,variable=Skin_Val) # Making a Radio Button For Choosing a Theme and assigning a value to it 
        self.green_button.configure(bg=framecolor) # Setting the Radiobuttons background to the frame color
        self.green_button.place(x=100,y=250) # Placing the Button on the Screen
        self.blue_button=Radiobutton(self.frame,text='Blue Skin',value=2,variable=Skin_Val) # Making a Radio Button For Choosing a Theme and assigning a value to it 
        self.blue_button.configure(bg=framecolor) # Setting the Radiobuttons background to the frame color
        self.blue_button.place(x=100,y=300) # Placing the Button on the Screen
        self.default_button=Radiobutton(self.frame,text='Default Skin',value=3,variable=Skin_Val) # Making a Radio Button For Choosing a Theme and assigning a value to it 
        self.default_button.configure(bg=framecolor) # Setting the Radiobuttons background to the frame color
        self.default_button.place(x=100,y=350) # Placing the Button on the Screen
        self.change_skin=Button(self.frame,text='CHANGE',command=change) # Making the Change button for changing the theme 
        self.change_skin.configure(bg=buttoncolor) # Setting the Background color of the buuton color
        self.change_skin.place(x=100,y=400) # Placing the button on the screen 

        
# Making a class called command screen for the assistant 
class CommandScreen:
    def __init__(self,master):
    
    #========== W I N D O W ==========#

        # Making the Window
        self.master=master # Making a Callable Master Variable
        self.master.geometry('600x600') # Setting the Screen Size (widthxheight)
        self.master.resizable(0,0) # Not allowing the User to Resize
        self.master.title('J.E.N Assistant') # Giving the Title for the Screen (in titlebar
        self.master.configure(bg=backgroundcolor) # Setting the background color

    #========== H E A D I N G  &   F R A M E ==========#

        # Setting the Heading or Making the Heading
        self.heading=Label(self.master,text='J.E.N Assistant',font=('Rockwell',30,'bold')) # Creating a Label which will be inside the window(Heading indide the screen)
        self.heading.configure(bg=backgroundcolor) # Setting background color 
        self.heading.pack() # Placing the  heading inside the window

        # Creating the Frame to Place the buttons
        self.frame=Frame(self.master,height=520,width=520,bd=10,relief=GROOVE) # Creating a Frame Inside the Screen
        self.frame.configure(bg=framecolor) # Setting the Colour for the Frame
        self.frame.pack() # Placing the  Frame inside the window


    # ========== B U T T O N S ==========#

        # Making the find phone button to perform the find phone function

        self.find_phone_button=Button(self.frame,text='FIND PHONE',width=10,height=5,font=('',12,'bold'),command=self.find_phone) # Making a Button for performing the find phone Function
        self.find_phone_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.find_phone_button.place(x=10,y=20) # Placing the Button on the Screen of the Assistant

        #  Making a Math button to perform math function which will take place in another window

        self.math_button=Button(self.frame,text='MATH',width=10,height=5,font=('',12,'bold'),command=self.math) # Making a Button for performing  the Math Function
        self.math_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.math_button.place(x=130,y=20) # Placing the Button on the Screen of the Assistant

        # Making the day button so that the assistant can tell you the day

        self.day_button=Button(self.frame,text='DAY',width=10,height=5,font=('',12,'bold'),command=day) # Making a Button for performing the Day Function 
        self.day_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.day_button.place(x=250,y=20) # Placing the Button on the Screen of the Assistant

        # Creating the date Function so that the assistant can tell you the date

        self.date_button=Button(self.frame,text='DATE',width=10,height=5,font=('',12,'bold'),command=date) # Making a Button for performing the Date Function 
        self.date_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.date_button.place(x=370,y=20) # Placing the Button on the Screen of the Assistant

        # Creating the timer button so that the assistant can set timer 

        self.timer_button=Button(self.frame,text='TIMER',width=10,height=5,font=('',12,'bold'),command=self.timer) # Making a Button for performing the Timer Function 
        self.timer_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.timer_button.place(x=370,y=140) # Placing the Button on the Screen of the Assistant

        # Creating the Time Button so that the assistant can tell you the current time

        self.time_button=Button(self.frame,text='TIME',width=10,height=5,font=('',12,'bold'),command=time_) # Making a Button for performing the Time Function 
        self.time_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.time_button.place(x=250,y=140) # Placing the Button on the Screen of the Assistant

        # Making the Camera button so that the assistant can open the camera (WEBCAM) for you

        self.camera_button=Button(self.frame,text='CAMERA',width=10,height=5,font=('',12,'bold'),command=camera) # Making a Button for performing the Camera Function 
        self.camera_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.camera_button.place(x=130,y=140) # Placing the Button on the Screen of the Assistant

        # Making the Draw Button so that the assistant can open the drawing app

        self.draw_button=Button(self.frame,text='DRAW',width=10,height=5,font=('',12,'bold'),command=draw) # Making a Button for performing the draw Function 
        self.draw_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.draw_button.place(x=10,y=140) # Placing the Button on the Screen of the Assistant

        # Making the play button so that the assistant can Playmusic from the givem directory

        self.play_music_button=Button(self.frame,text='PLAY MUSIC',width=10,height=5,font=('',12,'bold'),command=self.music) # Making a Button for performing the music Function 
        self.play_music_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.play_music_button.place(x=10,y=260) # Placing the Button on the Screen of the Assistant

        # Making the game button so that the assistant can open the game so that you
        # play when you are bored

        self.game_button=Button(self.frame,text='GAME',width=10,height=5,font=('',12,'bold'),command=game) # Making a Button for performing the Game Function 
        self.game_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.game_button.place(x=130,y=260) # Placing the Button on the Screen of the Assistant

        # Making the information button so that the assistant can get the information you want

        self.info_button=Button(self.frame,text='INFO',width=10,height=5,font=('',12,'bold'),command=self.info) # Making a Button for performing the Info Function 
        self.info_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.info_button.place(x=250,y=260) # Placing the Button on the Screen of the Assistant

        # Creating the SMS button so that the the assistant can send SMS to your Phone

        self.SMS_button=Button(self.frame,text='SMS',width=10,height=5,font=('',12,'bold'),command=self.sms) # Making a Button for performing the sms Function 
        self.SMS_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.SMS_button.place(x=370,y=260) # Placing the Button on the Screen of the Assistant

       
        # Creating the Map button so that the assistant can open Google Maps

        self.map_button=Button(self.frame,text='MAPS',width=10,height=5,font=('',12,'bold'),command=map_) # Making a Button for performing the Maps Function 
        self.map_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.map_button.place(x=10,y=380) # Placing the Button on the Screen of the Assistant

        # Creating the Google button so that the assistant can open Google

        self.google_button=Button(self.frame,text='GOOGLE',width=10,height=5,font=('',12,'bold'),command=open_google) # Making a Button for performing the Google Function 
        self.google_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.google_button.place(x=130,y=380) # Placing the Button on the Screen of the Assistant

        # Making the Write button so that you can write into the file

        self.write_button=Button(self.frame,text='WRITE',width=10,height=5,font=('',12,'bold'),command=self.j_write) # Making a Button for performing the write Function 
        self.write_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.write_button.place(x=250,y=380) # Placing the Button on the Screen of the Assistant

        # Creating the shutdown button so that you can shutdown your computer.

        self.shutdown_button=Button(self.frame,text='SHUTDOWN',width=10,height=5,font=('',12,'bold'),command=shutdown) # Making a Button for performing the Shutdown Function 
        self.shutdown_button.configure(bg=buttoncolor) # Setting the background color of the Button according to  the Theme
        self.shutdown_button.place(x=370,y=380) # Placing the Button on the Screen of the Assistant

        # Using .mainloop() to keep the window open

        self.master.mainloop()


    #========== F U N C T I O N S ==========#

    #  Making the Find phone function so that it opens a new window
    def find_phone(self):
        self.find_phone_w=Toplevel(self.master)
        self.app=FindPhoneScreen(self.find_phone_w)

    # Making the Math Function so that it performs calculations in a seperate window
    def math(self):
        self.math_w=Toplevel(self.master)
        self.app=MathWindow(self.math_w)

    #  Making the time Function so that it sets timer in a seperate window
    def timer(self):
        self.timer_w=Toplevel(self.master)
        self.app=TimerWindow(self.timer_w)

    # Making the Email Function so that it Sends email from a seperate window   
    def email(self):
        self.email_w=Toplevel(self.master)
        self.app=EmailWindow(self.email_w)

    # Making the info Function so that it asks you the topic and tell information in a seperate window
    def info(self):
        self.info_w=Toplevel(self.master)
        self.app=InfoWindow(self.info_w)
    

    # Making the Math Function so that it can send SMS from a seperate window
    def sms(self):
        self.sms_w=Toplevel(self.master)
        self.app=SMSWindow(self.sms_w)
        
    #  Making the Math Function so that you can write or assign it to write from a seperate window   
    def j_write(self):
        self.Writ_w=Toplevel(self.master)
        self.app=WritWindow(self.Writ_w)

    # Making the Math Function so that it Plays Music 
    def music(self):
        musicdir=askdirectory()
        play_music(music_dir=musicdir)


# Making a class called FindPhoneScreen for the Assistant  
class FindPhoneScreen:
    def __init__(self,master):

    #========== W I N D O W ==========#

        self.master=master # Making a Callable Master Variable
        self.master.geometry('400x400') # Setting Screen Size
        self.master.resizable(0,0) # Not Allowing the user to resize the window
        self.master.title('Find Phone Window') # Setting the Title for the Screen (Title bar)
        self.master.configure(bg=backgroundcolor) # Setting Background Color

    #========== H E A D I N G  &   F R A M E ==========#

        # Setting the Heading or Making the Heading
        self.heading=Label(self.master,text='Find Phone',font=('Rockwell',20,'bold')) # Creating a Label which will be inside the window(Heading indide the screen)
        self.heading.configure(bg=backgroundcolor) # Setting background color
        self.heading.pack() # Placing the  heading inside the window

        # Creating the Frame to Place the Elements
        self.frame=Frame(self.master,height=320,width=320,bd=10,relief=GROOVE) # Creating a Frame Inside the Screen
        self.frame.configure(bg=framecolor) # Setting the Colour for the Frame
        self.frame.pack() # Placing the  Frame inside the window

    # ========== B U T T O N S   ,   L A B E L S   &   E N T R Y ==========#
        
        # Setting the Heading or Making the Find Phone Label
        self.find_phone_label=Label(self.frame,text='Enter Phone Number :') # Creating a Label which will be inside the window(Label indide the Frame)
        self.find_phone_label.configure(bg=framecolor) # Setting background color
        self.find_phone_label.place(x=10,y=20) # Placing the  Label inside the window

        # Creating a Variable to Store the Value of a phonenumber in as string
        self.phone_number=StringVar()

        # Creating an Entry Field to take input
        self.find_phone_entry=Entry(self.frame,textvariable=self.phone_number) # Setting the Variable for the input Field
        self.find_phone_entry.place(x=150,y=20) # Placing the Input Field in the frame 

        #  Creating a Button For Performing the Find phone Function
        self.find_phone_button=Button(self.frame,text='Find Phone',width=10,command=self.find) # Making the Button and setting the Function or command to find the phone number
        self.find_phone_button.configure(bg=buttoncolor) # Setting the background color for the button
        self.find_phone_button.place(x=120,y=150) # Placing the  Button inside the window

    #========== F U N C T I O N S ==========#

    # Creating a Function Named find to find the phone number provided in the input field
    def find(self):
        phone=self.phone_number.get()
        find_phone(phone)


# Making a class called MathWindow for the Assistant 
class MathWindow:
    def __init__(self,master):

    #========== W I N D O W ==========#

        self.master=master # Making a Callable Variable called master
        self.master.geometry('400x400') # Setting the Screen Size
        self.master.resizable(0,0) # Not Allowing the USer to Resize the Window
        self.master.title('Math Window') # Giving the Title Or Name for the Titlebar of the Window
        self.master.configure(bg=backgroundcolor) # Setting the Screen Background Color

    #========== H E A D I N G  &   F R A M E ==========#

        # Setting the Heading or Making the Heading
        self.heading=Label(self.master,text='Math',font=('Rockwell',20,'bold')) # Creating a Label For the Heading of The Screen
        self.heading.configure(bg=backgroundcolor) # Setting the Backgroundcolor for the label 
        self.heading.pack() # Placing the Heading inside the window
        
        # Creating the Frame to Place the Elements
        self.frame=Frame(self.master,height=320,width=320,bd=10,relief=GROOVE) # Creating a Frame
        self.frame.configure(bg=framecolor) # Setting the Backgroundcolor for the frame
        self.frame.pack() # Placing the Frame inside the window
    
    
    # ========== B U T T O N S   ,   L A B E L S   &   E N T R Y ==========#
        
        #  Creating a Button For Performing the Statistics Function
        self.stat_button=Button(self.frame,text='Statistics',width=10,command=self.stat) # Making the Button and setting the Function or command to perform statistics
        self.stat_button.configure(bg=buttoncolor) # Setting the Background color of the button
        self.stat_button.place(x=10,y=20) # Placing the button on the window or screen

        self.cal_button=Button(self.frame,text='Calculations',width=10,command=self.cal) # Making the Button and setting the Function or command to perform calculations
        self.cal_button.configure(bg=buttoncolor) # Setting the Background color of the button
        self.cal_button.place(x=200,y=20) # Placing the button on the window or screen

    #========== F U N C T I O N S ==========#

    # Creating a Function Named stat to perform statistics function
    def stat(self):

        # Creating the function for the statistics-submit button
        def stat_submit():
            values=self.values.get() # Getting the Value of the Variable
            statask=self.statask.get() # Getting the Value of the Variable
            do_statistics(values,statask) # Performing thedo_statistics function

        # Creating a Label on the screen 
        self.statvalue_label=Label(self.frame,text='Enter Values :') # Creating a Label which will be inside the window(Label indide the Frame)
        self.statvalue_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.statvalue_label.place(x=10,y=70) # Placing the Label on the Screen 

        # Creating Variable to take values and Operations such as Mean Median or Mode.
        # Both are taken in the Form of String
        self.values=StringVar()
        self.statask=StringVar()

        # Creating a Entry or Input field on the screen 
        self.statvalue_entry=Entry(self.frame,textvariable=self.values) # Creating the Input Field and setting the text variable as values to take numbers
        self.statvalue_entry.place(x=115,y=70) # Placing the Input field or Entry on the Screen

        # Creating a Label on the screen 
        self.statask_label=Label(self.frame,text='Enter Operation :') # Creating a Label which will be inside the window(Label indide the Frame)
        self.statask_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.statask_label.place(x=10,y=100) # Placing the Label on the Screen 

        # Creating a Entry or Input field on the screen 
        self.statask_entry=Entry(self.frame,textvariable=self.statask) # Creating the Input Field and setting the text variable as statask to take values such as Mean , Median or Mode
        self.statask_entry.place(x=115,y=100)# Placing the Input field or Entry on the Screen

        #  Creating a Button For Performing the stat_submit Function 
        self.stat_submit_button=Button(self.frame,text='Submit',command=stat_submit) # Making the Button and setting the Function or command to statistics of the given data
        self.stat_submit_button.configure(bg=buttoncolor) # Setting the Background color of the button
        self.stat_submit_button.place(x=45,y=120) # Placing the Button on the Screen



    # Creating a Function Named stat to perform calculations function
    def cal(self):

        # Creating the function for the calculations-submit button
        def cal_submit():
            num1=self.firstvalue.get() # Getting the Value from the Variable
            num2=self.secondvalue.get() # Getting the Value from the Variable
            op=self.operation.get() # Getting the Value from the Variable
            calculation(num1,num2,op) # Performing the Do_calculations Functions using these values


        # Creating a Label on the screen     
        self.firstvalue_label=Label(self.frame,text='First Number :') # Creating a Label which will be inside the window(Label indide the Frame)
        self.firstvalue_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.firstvalue_label.place(x=10,y=70) # Placing the Label on the screen

        # Taking the First No. and second number in the form of integer
        # Taking the operation as a string variable
        self.firstvalue=IntVar()
        self.secondvalue=IntVar()
        self.operation=StringVar()

        # Creating a Entry or Input field on the screen
        self.firstvalue_entry=Entry(self.frame,textvariable=self.firstvalue) # Creating the Input Field and setting the text variable as firstvalue to take numbers
        self.firstvalue_entry.place(x=115,y=70) # Placing the Input Field on the Screen

        # Creating a Label on the screen
        self.secondvalue_label=Label(self.frame,text='Second Number :') # Creating a Label which will be inside the window(Label indide the Frame)
        self.secondvalue_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.secondvalue_label.place(x=10,y=100) # Placing the Label on the screen

        # Creating a Entry or Input field on the screen
        self.second_entry=Entry(self.frame,textvariable=self.secondvalue) # Creating the Input Field and setting the text variable as secondvalue to take numbers
        self.second_entry.place(x=115,y=100) # Placing the Input Field on the Screen

        # Creating a Label on the screen
        self.op_label=Label(self.frame,text='Enter Operation :') # Creating a Label which will be inside the window(Label indide the Frame)
        self.op_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.op_label.place(x=10,y=130) # Placing the Label on the screen

        # Creating a Entry or Input field on the screen
        self.op_entry=Entry(self.frame,textvariable=self.operation)  # Creating the Input Field and setting the text variable operation to take operation
        self.op_entry.place(x=115,y=130) # Placing the Input Field on the Screen

        #  Creating a Button For Performing the cal_submit Function 
        self.cal_submit_button=Button(self.frame,text='Submit',command=cal_submit) # Making the Button and setting the Function or command to calculate of the given data
        self.cal_submit_button.configure(bg=buttoncolor) # Setting the Background color of the button
        self.cal_submit_button.place(x=55,y=160) # Placing the Button on the Screen


# Making a class called ChatWindow for the Assistant 
class ChatWindow:

    def __init__(self,master):

    #========== W I N D O W ==========#

        self.master=master # Making a Callable Variable called master
        self.master.geometry('400x400') # Setting the Screen Size
        self.master.resizable(0,0) # Not Allowing the USer to Resize the Window
        self.master.title('Chat Window') # Giving the Title Or Name for the Titlebar of the Window
        self.master.configure(bg=backgroundcolor) # Setting the Screen Background Color

    #========== H E A D I N G  &   F R A M E ==========#

        # Setting the Heading or Making the Heading
        self.heading=Label(self.master,text='Chat',font=('Rockwell',20,'bold')) # Creating a Label For the Heading of The Screen
        self.heading.configure(bg=backgroundcolor) # Setting the Backgroundcolor for the label 
        self.heading.pack()# Placing the Heading inside the window

        # Creating the Frame to Place the Elements
        self.frame=Frame(self.master,height=320,width=320,bd=10,relief=GROOVE)# Creating a Frame
        self.frame.configure(bg=framecolor) # Setting the Backgroundcolor for the frame
        self.frame.pack() # Placing the Frame inside the window

    # ========== B U T T O N S   ,   L A B E L S   &   E N T R Y ==========#

        # Creating a Label on the screen 
        self.chat_label=Label(self.frame,text='You :') # Creating a Label which will be inside the window(Label indide the Frame)
        self.chat_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.chat_label.place(x=10,y=100)  # Placing the Label on the Screen 

        # Creating Variable to take input from the user as a string
        self.you_text=StringVar()

        # Creating a Entry or Input field on the screen
        self.chat_entry=Entry(self.frame,textvariable=self.you_text) # Creating the Input Field and setting the text variable as you_text to take chat input
        self.chat_entry.place(x=110,y=105) # Placing the input field on the screen

        #  Creating a Button For Performing the Statistics Function
        self.chat_button=Button(self.frame,text='Chat!',command=self.sendchat) # Making the Button and setting the Function or command to chat  
        self.chat_button.configure(bg=buttoncolor) # Setting the Background color of the button
        self.chat_button.place(x=100,y=150)
    
    #========== F U N C T I O N S ==========#
    
    # Creating a Function Named sendchat to perform chat function
    def sendchat(self):
        you=self.you_text.get()
        chat(you)


# Making a class called ChatWindow for the Assistant   
class InfoWindow:

    def __init__(self,master):

    #========== W I N D O W ==========#

        self.master=master # Making a Callable Variable called master
        self.master.geometry('400x400')  # Setting the Screen Size
        self.master.resizable(0,0) # Not Allowing the USer to Resize the Window
        self.master.title('Information Window') # Giving the Title Or Name for the Titlebar of the Window
        self.master.configure(bg=backgroundcolor)  # Setting the Screen Background Color

    #========== H E A D I N G  &   F R A M E ==========#

        # Setting the Heading or Making the Heading
        self.heading=Label(self.master,text='Information',font=('Rockwell',20,'bold'))# Creating a Label For the Heading of The Screen
        self.heading.configure(bg=backgroundcolor)  # Setting the Backgroundcolor for the label 
        self.heading.pack() # Placing the Heading inside the window

        # Creating the Frame to Place the Elements
        self.frame=Frame(self.master,height=320,width=320,bd=10,relief=GROOVE) # Creating a Frame
        self.frame.configure(bg=framecolor)  # Setting the Backgroundcolor for the frame
        self.frame.pack() # Placing the Frame inside the window

    # ========== B U T T O N S   ,   L A B E L S   &   E N T R Y ==========#
        
        # Creating a Label on the screen 
        self.info_label=Label(self.frame,text='Information About What :') # Creating a Label which will be inside the window(Label indide the Frame)
        self.info_label.configure(bg=framecolor)  # Setting the background color for the Labels
        self.info_label.place(x=10,y=100) # Placing the Label on the Screen 

        # Creating Variable to take what the user want ot get information about
        # It is String Datatype
        self.info=StringVar()

        # Creating a Entry or Input field on the screen
        self.info_entry=Entry(self.frame,textvariable=self.info)# Creating the Input Field and setting the text variable as info
        self.info_entry.place(x=150,y=105)# Placing the Input field or Entry on the Screen


        #  Creating a Button For Performing the stat_submit Function
        self.info_button=Button(self.frame,text='Find',command=self.search)  # Making the Button and setting the Function or command to search for the given data
        self.info_button.configure(bg=buttoncolor)# Setting the Background color of the button
        self.info_button.place(x=100,y=150)# Placing the Button on the Screen

    #========== F U N C T I O N S ==========# 

    # Creating a Function Named search to perform information function      
    def search(self):
        info=self.info.get()
        information(info)      


# Making a class called ChatWindow for the Assistant 
class SMSWindow:

    def __init__(self,master):

    #========== W I N D O W ==========#

        self.master=master # Making a Callable Variable called master
        self.master.geometry('400x400') # Setting the Screen Size
        self.master.resizable(0,0) # Not Allowing the USer to Resize the Window
        self.master.title('SMS Window') # Giving the Title Or Name for the Titlebar of the Window
        self.master.configure(bg=backgroundcolor) # Setting the Screen Background Color


    #========== H E A D I N G  &   F R A M E ==========#

       # Setting the Heading or Making the Heading
        self.heading=Label(self.master,text='SMS',font=('Rockwell',20,'bold')) # Creating a Label For the Heading of The Screen
        self.heading.configure(bg=backgroundcolor) # Setting the Backgroundcolor for the label 
        self.heading.pack() # Placing the Heading inside the window
        
        # Creating the Frame to Place the Elements
        self.frame=Frame(self.master,height=320,width=320,bd=10,relief=GROOVE) # Creating a Frame
        self.frame.configure(bg=framecolor) # Setting the Backgroundcolor for the frame
        self.frame.pack() # Placing the Frame inside the window

    # ========== B U T T O N S   ,   L A B E L S   &   E N T R Y ==========#
        
        #  Creating a Button For Performing the Statistics Function
        self.sms_label=Label(self.frame,text='Enter Message:') # Creating a Label which will be inside the window(Label indide the Frame)
        self.sms_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.sms_label.place(x=10,y=70)  # Placing the Label on the Screen 

        # Creating Variable to take message from the user
        # It is taken in the form of string
        self.text=StringVar()

        # Creating a Entry or Input field on the screen
        self.sms_entry=Entry(self.frame,textvariable=self.text) # Creating the Input Field and setting the text variable totext to take message
        self.sms_entry.place(x=100,y=70) # Placing the Input Field on the Screen
        
        #  Creating a Button For Performing the send sms Function 
        self.sms_button=Button(self.frame,text='Send',command=self.sendsms)# Making the Button and setting the Function or command to calculate of the given data
        self.sms_button.configure(bg=buttoncolor) # Setting the Background color of the button
        self.sms_button.place(x=110,y=100) # Placing the Button on the Screen

    #========== F U N C T I O N S ==========#

    # Creating a Function Named sendsms to send sms
    def sendsms(self):
        message=self.text.get()
        sms(message)


# Making a class called ChatWindow for the Assistant 
class WritWindow:

    def __init__(self,master):

    #========== W I N D O W ==========#

        self.master=master # Making a Callable Variable called master
        self.master.geometry('400x400') # Setting the Screen Size
        self.master.resizable(0,0) # Not Allowing the USer to Resize the Window
        self.master.title('Writing Window') # Giving the Title Or Name for the Titlebar of the Window
        self.master.configure(bg=backgroundcolor) # Setting the Screen Background Color
    
    #========== H E A D I N G  &   F R A M E ==========#
        
                # Setting the Heading or Making the Heading
        self.heading=Label(self.master,text='Writing',font=('Rockwell',20,'bold')) # Creating a Label For the Heading of The Screen
        self.heading.configure(bg=backgroundcolor) # Setting the Backgroundcolor for the label 
        self.heading.pack() # Placing the Heading inside the window
        
        # Creating the Frame to Place the Elements
        self.frame=Frame(self.master,height=320,width=320,bd=10,relief=GROOVE) # Creating a Frame
        self.frame.configure(bg=framecolor) # Setting the Backgroundcolor for the frame
        self.frame.pack() # Placing the Frame inside the window
    
    # ========== B U T T O N S   ,   L A B E L S   &   E N T R Y ==========#

        #  Creating a Button For Performing the self write Function
        self.self_writ_button=Button(self.frame,text='Self Write',command=self.self_writ) # Making the Button and setting the Function or command to perform self write function
        self.self_writ_button.configure(bg=buttoncolor) # Setting the Background color of the button
        self.self_writ_button.place(x=10,y=20)# Placing the button on the window or screen

        #  Creating a Button For Performing the autowrite Function
        self.auto_writ_button=Button(self.frame,text='Auto Write',command=self.auto_writ) # Making the Button and setting the Function or command to perform auto write function
        self.auto_writ_button.configure(bg=buttoncolor) # Setting the Background color of the button
        self.auto_writ_button.place(x=200,y=20)# Placing the button on the window or screen
    
    #========== F U N C T I O N S ==========#

    # Creating a Function Named stat to perform self write function
    def self_writ(self):
        self_write()
        
    # Creating a Function Named stat to perform auto Write  function    
    def auto_writ(self):
        def autosubmit():
            text=self.text.get()
            auto_write(text)

        # Creating a Label on the screen     
        self.auto_writ_label=Label(self.frame,text='Enter Words:')  # Creating a Label which will be inside the window(Label indide the Frame)
        self.auto_writ_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.auto_writ_label.place(x=10,y=70)# Placing the Label on the Screen 

        # Creating Variable to take input from the user as a string
        self.text=StringVar()

        # Creating a Entry or Input field on the screen
        self.auto_writ_entry=Entry(self.frame,textvariable=self.text) # Creating the Input Field and setting the text variable as text to take chat input
        self.auto_writ_entry.place(x=100,y=70) # Placing the input field on the screen
        
        self.auto_write_button=Button(self.frame,text='Submit',command=autosubmit) # Making the Button and setting the Function or command to autosubmit
        self.auto_write_button.configure(bg=buttoncolor)# Setting the Background color of the button
        self.auto_write_button.place(x=110,y=100) # Setting the Background color of the button


# Making a class called ChatWindow for the Assistant 
class TimerWindow:
    def __init__(self,master):

    #========== W I N D O W ==========#

        self.master=master # Making a Callable Variable called master
        self.master.geometry('400x400') # Setting the Screen Size
        self.master.resizable(0,0) # Not Allowing the USer to Resize the Window
        self.master.title('Timer Window') # Giving the Title Or Name for the Titlebar of the Window
        self.master.configure(bg=backgroundcolor) # Setting the Screen Background Color

    #========== H E A D I N G  &   F R A M E ==========#

        # Setting the Heading or Making the Heading
        self.heading=Label(self.master,text='Timer',font=('Rockwell',20,'bold')) # Creating a Label For the Heading of The Screen
        self.heading.configure(bg=backgroundcolor) # Setting the Backgroundcolor for the label 
        self.heading.pack()# Placing the Heading inside the window

        # Creating the Frame to Place the Elements
        self.frame=Frame(self.master,height=320,width=320,bd=10,relief=GROOVE)# Creating a Frame
        self.frame.configure(bg=framecolor) # Setting the Backgroundcolor for the frame
        self.frame.pack() # Placing the Frame inside the window
    
    # ========== B U T T O N S   ,   L A B E L S   &   E N T R Y ==========#
    
        # Creating a Label on the screen
        self.timer_label=Label(self.frame,text='Enter Seconds:') # Creating a Label which will be inside the window(Label indide the Frame)
        self.timer_label.configure(bg=framecolor) # Setting the background color for the Labels
        self.timer_label.place(x=10,y=70)   # Placing the Label on the Screen 
  
        # Creating Variable to take input from the user as a string
        self.sec=StringVar()

        # Creating a Entry or Input field on the screen
        self.timer_entry=Entry(self.frame,textvariable=self.sec)# Creating the Input Field and setting the text variable as sec to take seconds input
        self.timer_entry.place(x=100,y=70) # Placing the input field on the screen

        #  Creating a Button For Performing the Timer Function
        self.set_button=Button(self.frame,text='Set Timer',command=self.set_timer)# Making the Button and setting the Function or command to timer
        self.set_button.configure(bg=buttoncolor)# Setting the Background color of the button
        self.set_button.place(x=110,y=100) # Placing the button on the screen
    
    #========== F U N C T I O N S ==========#

    # Creating a Function Named set_timer to perform timer function
    
    def set_timer(self):
        sec=self.sec.get()
        timer_(sec)
        showinfo('Time Out','{} Seconds is completed Successfully'.format(sec))
        
if __name__=='__main__':
    root=Tk()
    
    MainScreen(root)