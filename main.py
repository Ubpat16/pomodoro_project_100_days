import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_app():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    header['text'] = "Timer"
    header['fg'] = GREEN
    check_mark['text'] = ''
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        # If its the 8th rep
        header['text'] = 'Rest'
        header['fg'] = YELLOW
        count_down(long_break_sec)

    elif rep % 2 == 0:
        # if its 2nd/4th/6th rep:
        count_down(short_break_sec)
        header['text'] = 'Rest'
        header['fg'] = GREEN

    else:
        # if its the 1st/3rd/5th/7th
        header['text'] = 'Work'
        header['fg'] = RED
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # 00:00
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second <= 0 or count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(rep / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Header Label

header = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
header.grid(column=1, row=0)

# Start button

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

# Reset button

reset = Button(text="Reset", command=reset_app)
reset.grid(column=2, row=2)

# Check mark

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
