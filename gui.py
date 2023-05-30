from tkinter import *
import jokehandler
jokehand = jokehandler.Jokehandler("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single")

root = Tk()
root.title("Jokes")

#Storlek på fönster
root.geometry("1000x400")

#Skapar textfält
textbox = Text(root, height=10, width=100, font="Arial", background="magenta")

#Skapar label
header = Label(root, text="Dagens skämt!")
header.config(font=("Arial", 14))

def clickButton():
    textbox.delete("1.0", "end")
    t_joke = jokehand.getJoke()
    textbox.insert(INSERT, t_joke)

button_getjoke = Button(text="Hämta skämt", padx=6, pady=6, command=clickButton)
button_avsluta = Button(root, text="Stick och brinn", padx=6, pady=6, command=root.destroy)

header.pack()
textbox.pack()
button_getjoke.pack()
button_avsluta.pack()

root.mainloop()

