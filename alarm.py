from datetime import datetime
from time import sleep
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from threading import Thread

bg_color = 'black'
color1 = '#1ABC9C'
color2 = '#ffffff'
color3 = 'grey'

window = Tk()
window.title("")
window.geometry('550x285')
window.configure(bg=bg_color)

frame_header = Frame(window, width=550, height=8, bg=color1)
frame_header.grid(row=0, column=0)

frame_body = Frame(window, width=550, height=550, bg=bg_color)
frame_body.grid(row=1, column=0)

frame_footer = frame_header = Frame(window, width=550, height=8, bg=color1)
frame_footer.grid(row=1, column=0)

img = Image.open('img/alarm4.png')
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)
app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=50)

name = Label(frame_body, text='Alarm', height=1,
             font=('Ivy 18 bold'), bg=bg_color, fg=color1)
name.place(x=125, y=30)

style = ttk.Style()
style.theme_use('default')
style.configure("TCombobox", fieldbackground=color1, background=color1)

hour = Label(frame_body, text='hour', height=1,
             font=('Ivy 10 bold'), bg=bg_color, fg=color1)
hour.place(x=125, y=70)
c_hour = Combobox(frame_body, width=3, font='arial 15')
c_hour['values'] = ("00", "01", "02", "03", "04", "05",
                    "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=130, y=98)

min = Label(frame_body, text='min', height=1,
            font=('Ivy 10 bold'), bg=bg_color, fg=color1)
min.place(x=200, y=70)
c_min = Combobox(frame_body, width=3, font='arial 15')
c_min['values'] = ("00", "01", "02", "03", "04", "05",
                   "06", "07", "08", "09", "10", "11", "12",
                   "13", "14", "15", "16", "17", "18", "19",
                   "20", "21", "22", "23", "24", "25", "26",
                   "27", "28", "29", "30", "31", "32", "33",
                   "34", "35", "36", "37", "38", "39", "40",
                   "41", "42", "43", "44", "45", "46", "47",
                   "48", "49", "50", "51", "52", "53", "54",
                   "55", "56", "57", "58", "59")
c_min.current(0)
c_min.place(x=200, y=98)

sec = Label(frame_body, text='sec', height=1,
            font=('Ivy 10 bold'), bg=bg_color, fg=color1)
sec.place(x=270, y=70)
c_sec = Combobox(frame_body, width=3, font='arial 15')
c_sec['values'] = ("00", "01", "02", "03", "04", "05",
                   "06", "07", "08", "09", "10", "11", "12",
                   "13", "14", "15", "16", "17", "18", "19",
                   "20", "21", "22", "23", "24", "25", "26",
                   "27", "28", "29", "30", "31", "32", "33",
                   "34", "35", "36", "37", "38", "39", "40",
                   "41", "42", "43", "44", "45", "46", "47",
                   "48", "49", "50", "51", "52", "53", "54",
                   "55", "56", "57", "58", "59")
c_sec.current(0)
c_sec.place(x=270, y=98)

period = Label(frame_body, text='period', height=1,
               font=('Ivy 10 bold'), bg=bg_color, fg=color1)
period.place(x=340, y=70)
c_period = Combobox(frame_body, width=3, font='arial 15')
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=340, y=98)


def activate_alarm():
    t = Thread(target=alarm())
    t.start


# deactivate with distance moved
def deactivate_alarm():
    mixer.music.stop()


selected = IntVar()


rad1 = Radiobutton(frame_body, font=('arial 10 bold'),
                   value=1, text='Activate', bg=bg_color, fg=color1, command=activate_alarm, variable=selected)
rad1.place(x=125, y=135)


def alarm_sound():
    mixer.music.load('alarm.mp3')
    mixer.music.play()

    selected.set(0)
    rad2 = Radiobutton(frame_body, font=('arial 10 bold'),
                       value=2, text='Deactivate', bg=bg_color, fg=color1, command=deactivate_alarm, variable=selected)
    rad2.place(x=225, y=135)


def alarm():
    while True:
        control = selected.get()
        set_hr = c_hour.get()
        set_min = c_min.get()
        set_sec = c_sec.get()
        set_period = c_period.get()
        set_period = str(set_period).upper()

        print("set ", set_hr, " ", set_min, " ", set_sec)
        now = datetime.now()
        hr = now.strftime("%I")
        min = now.strftime("%M")
        sec = now.strftime("%S")
        period = now.strftime("%p")
        print("curr", hr, " ", min, " ", sec)

        if control == 1 and set_period == period and set_hr == hr and set_min == min and set_sec == sec:
            # print("BREAK TIME!")
            alarm_sound()
            break
        sleep(1)

mixer.init()
window.mainloop()
