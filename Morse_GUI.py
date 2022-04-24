#Import modules
import RPi.GPIO as GPIO
from tkinter import *
from time import sleep
import os


#Initialise output pin and GUI
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GUI = Tk()
GUI.title('Morse Code Blinker')


#Initialise duration of LED blinks
short_time = 0.25
long_time = 3 * short_time
end = long_time - short_time


#Function for short blink
def short():
    GPIO.output(11, GPIO.HIGH)
    sleep(short_time)
    GPIO.output(11, GPIO.LOW)
    sleep(short_time)
    
    
#Function for long blink
def long():
    GPIO.output(11, GPIO.HIGH)
    sleep(long_time)
    GPIO.output(11, GPIO.LOW)
    sleep(short_time)


#Function to blink letters of the alphabet in Morse code
def Morse_code(letter):
    if letter == 'a':
        short()
        long()
        sleep(end)
    elif letter == 'b':
        long()
        short()
        short()
        short()
        sleep(end)
    elif letter == 'c':
        long()
        short()
        long()
        short()
        sleep(end)
    elif letter == 'd':
        long()
        short()
        short()
        sleep(end)
    elif letter == 'e':
        short()
        sleep(end)
    elif letter == 'f':
        short()
        short()
        long()
        short()
        sleep(end)
    elif letter == 'g':
        long()
        long()
        short()
        sleep(end)
    elif letter == 'h':
        short()
        short()
        short()
        short()
        sleep(end)
    elif letter == 'i':
        short()
        short()
        sleep(end)
    elif letter == 'j':
        short()
        long()
        long()
        long()
        sleep(end)
    elif letter == 'k':
        long()
        short()
        long()
        sleep(end)
    elif letter == 'l':
        short()
        long()
        short()
        short()
        sleep(end)
    elif letter == 'm':
        long()
        long()
        sleep(end)
    elif letter == 'n':
        long()
        short()
        sleep(end)
    elif letter == 'o':
        long()
        long()
        long()
        sleep(end)
    elif letter == 'p':
        short()
        long()
        long()
        short()
        sleep(end)
    elif letter == 'q':
        long()
        long()
        short()
        long()
        sleep(end) 
    elif letter == 'r':
        short()
        long()
        short()
        sleep(end)
    elif letter == 's':
        short()
        short()
        short()
        sleep(end)
    elif letter == 't':
        long()
        sleep(end)
    elif letter == 'u':
        short()
        short()
        long()
        sleep(end)
    elif letter == 'v':
        short()
        short()
        short()
        long()
        sleep(end)
    elif letter == 'w':
        short()
        long()
        long()
        sleep(end)
    elif letter == 'x':
        long()
        short()
        short()
        long()
        sleep(end)
    elif letter == 'y':
        long()
        short()
        long()
        long()
        sleep(end)
    elif letter == 'z':
        long()
        long()
        short()
        short()
        sleep(end)


#Function to convert user input into an array of characters and make calls to Morse_code
def Convert():
    word = [char for char in user_input.get()]
    for letter in word:
        Morse_code(letter)


#Function to enforce character limit
def callback(sv):
    c = sv.get()[0:12]
    sv.set(c)

    
#Function to close the GUI    
def Close():
    GPIO.output(11, GPIO.LOW)
    GUI.destroy()


#Monitor user inputs to create a character limit
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))


#Create GUI elements
text = Label(GUI, text = ('Enter word to convert to Morse code' + os.linesep + '(max 12 characters)'))
user_input = Entry(GUI, width = 18, textvariable = sv)
convert = Button(GUI, text = 'Convert', command = Convert)
close = Button(GUI, text = 'Close', command = Close)


#Align GUI elements
text.pack(padx = 10, pady = 10)
user_input.pack()
convert.pack()
close.pack(pady = 10)


#Keep the window open until the 'Close' button is pressed 
mainloop()
