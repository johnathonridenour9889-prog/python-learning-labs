import tkinter as tk
import random as rnd

def _screen_():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("6 Side Dice")
    root.configure(bg='black')

    label = tk.Label(root, text="6 Side Dice!",bg='blue',fg='white', font=("Arial", 18))
    label.pack(pady=20 , padx=20)

    dice_rolled = tk.Label(root, text="?",bg='blue',fg= 'white',width=15, height=2, font=("Arial", 18))
    dice_rolled.pack(pady=125 , padx=125)

    def dice_roll():
        dice = rnd.randint(1, 6)
        dice_rolled.config(text=dice)

    button = tk.Button(root, text="Roll Dice", command=dice_roll, bg='blue',fg='white', width=20, height=4)
    button.pack()

    root.mainloop()

def main():
    _screen_()

if __name__ == "__main__":
    main()
