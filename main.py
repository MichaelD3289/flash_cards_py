from tkinter import *
import random

import pandas

# constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_FLIP_TIME = 3 * 1000

# globals
current_card = {}

# file
try:
    dataframe = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_data = original_data.to_dict(orient="records")
else:
    words_data = dataframe.to_dict(orient="records")


# functions
#   get new word
def next_card():
    global wait_time, current_card
    window.after_cancel(wait_time)

    flash_card.itemconfig(flash_card_img, image=card_front_img)

    current_card = random.choice(words_data)
    french_word = current_card['French']

    flash_card.itemconfig(display_word, text=french_word, fill="black")
    flash_card.itemconfig(display_title, text="French", fill="black")

    wait_time = window.after(CARD_FLIP_TIME, flip_card)


#   flip card to back side
def flip_card():
    flash_card.itemconfig(flash_card_img, image=card_back_img)

    flash_card.itemconfig(display_word, text=current_card['English'], fill="white")
    flash_card.itemconfig(display_title, text="English", fill="white")


#   Guessed card correctly
def guessed_right():
    words_data.remove(current_card)
    data = pandas.DataFrame(words_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# window
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
wait_time = window.after(250, next_card)

# images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# flash card
flash_card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_img = flash_card.create_image(400, 263, image=card_front_img)
display_title = flash_card.create_text(400, 150, text="", font=('Ariel', 40, "italic"))
display_word = flash_card.create_text(400, 263, text="", font=('Ariel', 60, "bold"))

# buttons
right_btn = Button(image=right_img, borderwidth=0, highlightthickness=0, command=guessed_right)
wrong_btn = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=next_card)

# grid
flash_card.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

window.mainloop()
