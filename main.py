from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# images
card_front = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")


# Flash Card
flash_card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.create_image(400, 263, image=card_front)

flash_card.create_text(400, 150, text="French", font=('Ariel', 40, "italic"))
flash_card.create_text(400, 263, text="trouve", font=('Ariel', 60, "bold"))

# Buttons
right_btn = Button(image=right_img, borderwidth=0)
wrong_btn = Button(image=wrong_img, borderwidth=0)

# Grid
flash_card.grid(row=0, column=0, columnspan=2)
right_btn.grid(row=1, column=1)
wrong_btn.grid(row=1, column=0)


window.mainloop()
