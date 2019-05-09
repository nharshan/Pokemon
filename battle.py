from pokemon import *
from move import *
from player import *




pokemon = Pokemon()

def battle(pokemon1, pokemon2):
    
        
        print ("\n"," *** Battle Begins ***", "\n")
        while(pokemon1.current_hp>0 and pokemon2.current_hp>0):
            pokemon1.attack(pokemon1.move,pokemon2)
            if pokemon2.current_hp<=0:
                break
            pokemon2.attack(pokemon2.move,pokemon1)
        
        if(pokemon1.current_hp<=0):
                print ("\n",pokemon2.name, "Won the Battle!")
            
        else:
            print("\n",pokemon1.name, "Won the battle!")


# Passing Default parameters for the function Pokemon

pokemon1 = Pokemon(111,'Pikachu',1,1,'Electric','None',move('Thunder Shock',8.33),move('Thunder Shock',8.33),7.42,0.47,'M',1.0)
pokemon2 = Pokemon(111,'Squirtle',1,1,'Water','None',move('Water Gun',5.0),move('Water Gun',5.0),7.42,0.47,'F',1.0)

# Randomizing Values for both the Pokemon objects

pokemon1.randomize_status()
pokemon2.randomize_status()


## Before attack Values

print('Before Attack :\n')
print(pokemon1)
print('\n')
print(pokemon2)
print('\n')

## Attack Functions

#print('Battle Started! \n')
battle(pokemon1,pokemon2)
        
        
