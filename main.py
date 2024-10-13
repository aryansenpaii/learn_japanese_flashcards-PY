from tkinter import *
import pandas
import random

try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data=pandas.read_csv("data/japanese_words.csv")
finally:
    to_learn = word_data.to_dict(orient="records")

current_card={}
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    current_card_word=current_card["Japanese"]
    canvas.itemconfig(language_title,text="Japanese",fill="black")
    canvas.itemconfig(word_text,text=f"{current_card_word}",fill="black")
    canvas.itemconfig(card_front,image=card_front_img)
    flip_timer=window.after(3000,flip_card)
def flip_card():
    current_choice_meaning=current_card["English"]
    canvas.itemconfig(language_title, text="English",fill="white")
    canvas.itemconfig(word_text, text=f"{current_choice_meaning}",fill="white")
    canvas.itemconfig(card_front,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    words_to_learn=pandas.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv",index=False)
    next_card()

BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.title("Flashy-JP")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)

card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")


card_front=canvas.create_image(400,263, image=card_front_img)

language_title=canvas.create_text(400,150,text="",font=('Ariel',40,"italic"))
word_text=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=cross_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=2,column=0)

tick_image=PhotoImage(file="images/right.png")
right_button=Button(image=tick_image,highlightthickness=0,command=is_known)
right_button.grid(row=2,column=1)
next_card()







window.mainloop()
