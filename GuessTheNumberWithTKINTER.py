# Graficni vmesnik za igro guess the secret number

# uvoz knjiznice, ki vsebuje potrebne metode za izdelavo graficnega vmesnika
import tkinter
import random
from tkinter import messagebox

# Inicializacija
window = tkinter.Tk()
secret = random.randint(1, 30)

# Velikost Okna
window.geometry("1000x500")

# Barva ozadja
window.configure(bg="blue")

#  Tekst - Pozdravni tekst
Greetings = tkinter.Label(window, text="Welcome to Guess the Secret game by Domen Kastelic !")
Greetings.pack()

# Dodajanje vnosnega polja
guess = tkinter.Entry(window)
guess.pack()

# Gumb (Submit/Potrdi)
# Metoda
def check_guess():
    if int(guess.get()) == secret:
        result_text = "Your guess is correct!"
    elif int(guess.get()) > secret:
        result_text = "Wrong! Your guess is too high!"
    else:
        result_text = "Wrong! Your number is too low!"

    # Prikaz messageBox
    messagebox.showinfo("Result", result_text)

# Gumb za potrditev vnesene vrednosti + barva ozadja in barva klika
submit = tkinter.Button(window, text="Check Answer", command = check_guess, bg="red", activebackground="green")
submit.pack()


# Program se izvaja v neskoncnost, dokler ga ne zapremo rocno
window.mainloop()

# Izboljsanje graficnega vmesnika -  dodajanje barv, velikost fonta, ozadje
# Pozicija elementov,...

# Zapri igro ce pravilen odg