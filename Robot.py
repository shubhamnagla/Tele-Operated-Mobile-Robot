from tkinter import *
import imutils
from PIL import ImageTk, Image
import os
import numpy as np
import cv2
from time import sleep
import RPi.GPIO as GPIO
from time import sleep

root = Tk()
root.geometry("800x600")
lmain = Label(root)
lmain.grid()
in1 = 23
in2 = 24
in3 = 17
in4 = 27
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)


p=GPIO.PWM(en,1000)
p.start(75)
b = Button(width = 10, height = 2, text = 'Forward')
b.grid(row = 1, column = 0)
b2 = Button(width = 10, height = 2, text = 'Reverse')
b2.grid(row = 1,column = 1)
b3 = Button(width = 10, height = 2, text = 'Right')
b3.grid(row = 2,column = 0)
b4 = Button(width = 10, height = 2, text = 'Left')
b4.grid(row = 2,column = 1)


video=cv2.VideoCapture(0)

def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    sleep(1)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    print("Moving Forward")
def reverse():
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)
    sleep(1)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("reverse")
def right():
    GPIO.output(in3,GPIO.HIGH)
    sleep(1)
    GPIO.output(in3,GPIO.LOW)
    print("Moving right")
def left():
    GPIO.output(in1,GPIO.HIGH)
    sleep(1)
    GPIO.output(in1,GPIO.LOW)
    print("Moving left")
def video_stream():
    ret, frame = video.read()
    frame= imutils.rotate(frame, 180) 
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 
b.config(command=forward)
b2.config(command=reverse)
b3.config(command=right)
b4.config(command=left)
video_stream()
root.mainloop()

