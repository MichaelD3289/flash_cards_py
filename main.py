from tkinter import *
import random

import pandas

# constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_FLIP_TIME = 3 * 1000

# globals
wait_time = None


# functions
#   get new word
def next_card():
    flash_card.itemconfig(flash_card_img, image=card_front_img)

    random_word = random.choice(words_data)
    french_word = random_word['French']

    flash_card.itemconfig(display_word, text=french_word, fill="black")
    flash_card.itemconfig(display_title, text="French", fill="black")

    english_word = random_word['English']

    global wait_time
    wait_time = window.after(CARD_FLIP_TIME, flip_card, "English", english_word)


#   flip card to English side
def flip_card(title, word):
    flash_card.itemconfig(flash_card_img, image=card_back_img)

    flash_card.itemconfig(display_word, text=word, fill="white")
    flash_card.itemconfig(display_title, text=title, fill="white")

    window.after_cancel(wait_time)


# window
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

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

flash_card.itemconfig(flash_card_img, image=card_front_img)

# buttons
right_btn = Button(image=right_img, borderwidth=0, highlightthickness=0, command=next_card)
wrong_btn = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=next_card)

# grid
flash_card.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

# file
dataframe = pandas.read_csv("data/french_words.csv")
words_data = dataframe.to_dict(orient="records")

window.mainloop()
