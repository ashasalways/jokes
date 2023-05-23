#https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single
import os
import jokehandler

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n-Torra historier-")

    url = f"https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"

    nr = 1
    jokeobjekt = jokehandler.Jokehandler(url)

    while True:

        tJoke = jokeobjekt.getJoke()

        print(f"\n{nr}.--------------------------------")
        print(f"{tJoke}")
        print("----------------------------------------")

        nr += 1

        entill = input("Vill du ha en till? Y/N ")

        if (entill == "n" or entill == "N"):
            break

        


main()