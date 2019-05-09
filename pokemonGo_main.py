from pokemon import *
from player import *
from item import  *
#from battle import *
import sqlite3
import database
import tkinter as tkk
from tkinter import *
from tkinter import messagebox
import time
import os
from tkinter.font import BOLD

### Main Tkinker root declaration ###
root = Tk()
root.title("Project: Pokemon GO")  # Tkinker window title
root.geometry('715x680')  # Tkinker window size
photo1 = PhotoImage(file="C:/Users/yogi_/Downloads/start1.gif")

#### Gif Image handler ####

frames = [PhotoImage(file='C:/Users/yogi_/Downloads/test8.gif',format = 'gif -index %i' %(i)) for i in range(0,63)]
def update(ind):
    if ind<63:
        frame = frames[ind]
        ind += 1
        label.configure(image=frame)
        root.after(100, update, ind)
    
label = Label(root)
label.pack()
root.after(0, update, 0)

 
#Label for Tkinker

lbl = Label(root, text="Click on the POKEBALL to play the game" + '\n', highlightthickness=3,font=("Rouge",20)).pack() 

### Start Button ###
def click():
    messagebox.showinfo('Your Game is Starting', 'Please input your Username and Password if you are a returining player')
    root.after(10, root.destroy)


btn = Button(root, text="Start",font=("Rouge",16),height=80,width=80,image=photo1, command=click).pack()
 
root.mainloop() # End Encapsulation for entire Tkinker


##### Main Program #####
def main_menu(player):
    menu_str="\nSelect an option below (input number 0~5):\n1: Catch pokemon\n"+\
             "2: Fight against another player\n"+\
             "3: Visit PokeStop\n"+\
             "4: View items in bag\n"+\
             "5: View pokemons in hand\n"+\
             "0: Save and Exit\n"
    print(menu_str)
    option=int(input())
    while (option!=0):
        if(option==1):
            player.enter_capture_module()
        elif(option==2):
            #pokemon1=generate_pokemon(1)
            #pokemon2=generate_pokemon_by_name("Pikachu")
            #battle(pokemon1, pokemon2)
            pass    
        elif(option==3):
            player.visit_pokestop()
        elif(option==4):
            print(player.username+"'s bag:\n")
            print(player.bag)
        elif(option==5):
            player.list_pokemons_in_hand()
        else:
            print("PLease only enter a number between 0~3.\n")
        option=int(input(menu_str))
    database.save_progress(player)
    print("Exiting....See you next time!\n")
    
  



def login_module():
    player_name=input("Enter  your name:\n")
    user_exist=database.check_username_in_database(player_name)
    if(user_exist):
        user_name, user_password, level, experience = database.get_user_info(player_name)
        while(input("Please enter your password:")!=user_password):
            print("Wrong password! Please Try again!")
        player=Player(user_name,user_password,experience,level)
        database.sync_from_db(player)
        print("\nWelcome back! Login completed.\n") 
    else:
        password=input("Welcome new player! Please create your password:")
        player=Player(player_name,password,0,1)
        database.create_new_player(player)
        for i in range(15):
            player.bag.add_item(PokeBall("Poke Ball"))
            player.bag.add_item(Potion("Potion"))
            player.bag.add_item(Revive("Revive"))
            player.bag.add_item(RazzBerry("Razz Berry"))
            player.bag.add_item(Candy("Rare candy"))
            player.bag.add_item(Candy("Sweet candy"))
            player.bag.add_item(Candy("Rainbow candy"))
            player.bag.add_item(Stardust("Silver dust"))
            player.bag.add_item(Stardust("Gold dust"))
            player.bag.add_item(Stardust("Diamond dust"))
        print("Welcome! You will start a new journey.")
        print("You are given Amazing starting items. Check your bag")
    return player    




        
new_player=login_module()            
main_menu(new_player)

            
player=Player(input("input your name:\n"),input("input password:\n"))

for i in range(5):
    player.bag.add_item(PokeBall("Ultra Ball"))
    player.bag.add_item(Potion("Potion"))
    player.bag.add_item(Revive("Revive"))
    player.bag.add_item(RazzBerry("Razz Berry"))
    player.bag.add_item(Candy("skittles candy"))
    player.bag.add_item(Candy("twizzlers candy"))
    player.bag.add_item(Candy("cadbury candy"))
    player.bag.add_item(Stardust("helium dust"))
    player.bag.add_item(Stardust("neon dust"))
    player.bag.add_item(Stardust("hydrogen dust"))


pokemon1=generate_pokemon(1)
player.pokemons_in_hand.append(pokemon1)
pokemon2=generate_pokemon(4)
player.pokemons_in_hand.append(pokemon2)
pokemon3=generate_pokemon_by_name("Pikachu")
player.encounter_pokemon(pokemon3)

print(pokemon1,"\n")
print(pokemon2,"\n")

pokemon3.attack(pokemon3.move, pokemon1)
pokemon2.current_hp=0
