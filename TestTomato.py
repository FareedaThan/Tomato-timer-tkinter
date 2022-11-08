from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    t = time.localtime()
    current_sec = t.tm_hour*3600+t.tm_min*60+t.tm_sec
    set_sec = 18*3600
    count_down(10)  #set_sec-current_sec


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_hour = count // 3600
    count_min = (count % 3600) // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_hour < 10:
        count_hour = f"0{count_hour}"
    canvas.itemconfig(timer_text, text=f"{count_hour}:{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
        # window.update()
        # canvas.itemconfig
        # print(window.winfo_geo metry().split("+")[0])
    else:
        canvas.itemconfig(tomato, image=tomato_bomb)


# ---------------------------- UI SETUP ------------------------------- #
#  create window
window = Tk()
window.title("Tomato")
window.geometry('500x500')
window.config(padx=100, pady=50, bg=YELLOW)

checkmark = "✔"
# Create text
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)  # position the text label on the grid

#  create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
tomato_bomb = PhotoImage(file="tomato_bomb1.png")
tomato = canvas.create_image(100, 113, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00:00", fill="white", font=(FONT_NAME, 25, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

# Create button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Create label
# check_marks = Label(text=checkmark, fg=GREEN, bg=YELLOW)
# check_marks.grid(column=1, row=3)


window.mainloop()
