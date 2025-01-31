from tkinter import *
import pandas
import random

# ---------------------------- DATA SETUP  ------------------------------- #
try:
    word_list = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    word_list = pandas.read_csv("./data/french_words.csv")

word_list_dict = word_list.to_dict(orient="records")
words = random.choice(word_list_dict)
# print(word_list_dict, word_list)
timer = ""

# ----------------------------  SAVE INCORRECT WORDS  ------------------------------- #
def save_word():
    global word_list_dict
    global words
    word_list_dict.remove(words)
    practice_words = {"French": item["French"] for item in word_list_dict}
    print(practice_words)
    change_word()

# ---------------------------- SHOW FRENCH WORD  ------------------------------- #
def change_word():
    global words
    global timer
    words = random.choice(word_list_dict)
    french_word = words["French"]
    card_canvas.itemconfigure(title, text="French", fill="black")
    card_canvas.itemconfigure(word, text=french_word, fill="black")
    card_canvas.itemconfigure(img, image=card_front_img)
    timer = window.after(3000, flip_card, words)


# ---------------------------- SHOW ENGLISH WORD  ------------------------------- #
def flip_card(word_dict):
    global timer
    window.after_cancel(timer)
    english_word = word_dict["English"]
    card_canvas.itemconfigure(title, text="English", fill="white")
    card_canvas.itemconfigure(word, text=english_word, fill="white")
    card_canvas.itemconfigure(img, image=card_back_img)

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

#Card
card_canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
img = card_canvas.create_image(400, 263)
title = card_canvas.create_text((400,150), font=("Arial", 40, "italic"))
word = card_canvas.create_text((400,263), font=("Arial", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)
change_word()


#Correct Button
correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=save_word)
correct_button.grid(column=0, row=1)

#Incorrect Button
incorrect_img = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=change_word)
incorrect_button.grid(column=1, row=1)



window.mainloop()
