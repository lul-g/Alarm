# Music by <a href="/users/microsammy-22905943/?tab=audio&amp;utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=audio&amp;utm_content=8761">Microsammy</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=8761">Pixabay</a>
from pygame import mixer
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from datetime import datetime
import time


window = Tk()
window.title("")
window.geometry('350x150')


def alarm():
    while True:
        # print(1)
        control = 1
        set_hr = '06'
        set_min = '58'
        set_sec = '20'
        set_period = 'pm'.upper()
        print("set ", set_hr, " ", set_min, " ", set_sec)
        now = datetime.now()
        hr = now.strftime("%I")
        min = now.strftime("%M")
        sec = now.strftime("%S")
        period = now.strftime("%p")
        print("curr", hr, " ", min, " ", sec)

        if control == 1 and set_period == period and set_hr == hr and set_min == min and set_sec == sec:
            print("BREAK TIME!")
            alarm_sound()
            break
        time.sleep(1)


def alarm_sound():
    mixer.music.load('alarm.mp3')
    mixer.music.play()


mixer.init()
alarm()

window.mainloop()
