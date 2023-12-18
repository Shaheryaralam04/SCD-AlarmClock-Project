from tkinter import *
from time import strftime
import datetime
import time
import pygame

root = Tk()
root.title("Digital Clock by For SCD Project")
root.geometry("500x300")
root.configure(bg="black")

# Digital Clock
def clock():
    string = strftime("%H:%M:%S")
    month = strftime("%B")
    month1 = strftime("%m")
    year = strftime("%Y")
    day = strftime("%A")

    my_label1.config(text=string)
    my_label1.after(1000, clock)

    my_label2.config(text=month + month1 + " " + year + "          " + day)

my_label1 = Label(root, text="", font=("Digital-7 Mono", 90), bg="black", fg="cyan", relief=SUNKEN)
my_label1.pack(pady=30)

my_label2 = Label(root, font=("Digital-7 Mono", 21), bg="black", fg="white")
my_label2.pack()
clock()

pygame.mixer.init()

def open():
    window = Toplevel()
    window.title("Alarm Window")
    window.geometry("400x200")
    window.configure(bg="white")
    time_format = Label(window, text="Enter time in 24 hour format!", fg="red", bg="black", font="Arial").place(x=70, y=120)

    e1 = Entry(window, text=hour, width=10, bd=2)
    e1.place(x=90, y=40)
    e1.insert(0, "HOUR")
    e2 = Entry(window, text=min, width=10, bd=2)
    e2.place(x=160, y=40)
    e2.insert(0, "MIN")
    e3 = Entry(window, text=sec, width=10, bd=2)
    e3.place(x=230, y=40)
    e3.insert(0, "SEC")

    submit = Button(window, text="SET ALARM", font=("Helevetica", 10, "bold"), width=10, fg="cyan", bg="black", command=actual_time).place(x=150, y=80)

    stop_btn = Button(window, text="STOP ALARM", font=("Helevetica", 10, "bold"), width=10, fg="cyan", bg="black", command=stop).place(x=150, y=160)

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            pygame.mixer.music.load("Alarm-ringtone.mp3")
            pygame.mixer.music.play()
            break

#variables for set alarm
hour = StringVar()
min = StringVar()
sec = StringVar()

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

def stop():
    pygame.mixer.music.stop()

my_button = Button(root, text="ALARM", font=("Helevetica", 12, "bold"), bg="black", fg="red", command=open)
my_button.pack(pady=15)

mainloop()
