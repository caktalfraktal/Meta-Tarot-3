import tkinter as tk
import os
from tarot_deck import tarot_deck
import random
def draw_cards():
    random.SystemRandom().shuffle(tarot_deck)
    card1 = tarot_deck[int.from_bytes(os.urandom(3), 'big') % len(tarot_deck)]
    tarot_deck.remove(card1)
    card2 = tarot_deck[int.from_bytes(os.urandom(3), 'big') % len(tarot_deck)]
    tarot_deck.remove(card2)
    card3 = tarot_deck[int.from_bytes(os.urandom(3), 'big') % len(tarot_deck)]
    tarot_deck.remove(card3)
    card1_image = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), card1['image']))
    card2_image = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), card2['image']))
    card3_image = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), card3['image']))
    card_meanings = f"Card 1: {card1['name']} - {card1['meaning']}\nCard 2: {card2['name']} - {card2['meaning']}\nCard 3: {card3['name']} - {card3['meaning']}"
    return card1_image, card2_image, card3_image, card_meanings
def main():
    root = tk.Tk()
    root.title("Tarot Card Reader")
    card1_image, card2_image, card3_image, card_meanings = draw_cards()
    label1 = tk.Label(root, image=card1_image)
    label1.grid(row=0, column=0)
    label2 = tk.Label(root, image=card2_image)
    label2.grid(row=0, column=1)
    label3 = tk.Label(root, image=card3_image)
    label3.grid(row=0, column=2)
    label_text = tk.Label(root, text=card_meanings, wraplength=400)
    label_text.grid(row=1, column=0, columnspan=3)
    separator = tk.Frame(height=10, bd=1)
    separator.grid(row=2, column=0, columnspan=3)
    root.mainloop()
if __name__ == "__main__":
    main()