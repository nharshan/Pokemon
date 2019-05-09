from player import *
import requests


def getGoogleData():
    request_str = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Massachusetts&types=(cities)&key=AIzaSyAyoWh3bL8Odto5oXOG00Hw2qAT96MwMkk"
           
    
    
    #Getting response
    
    response=requests.get(request_str)
    
    num_of_stops=len(response.json()['predictions'])
    
    if(num_of_stops>0):
    
                print("Select a place to visit:\n")
    
                for i in range(num_of_stops):
    
                    print(i+1,":",response.json()['predictions'][i]['description'])                
    
                user_selection=int(input())
    
                location=response.json()['predictions'][user_selection-1]
    
           
    
                print("You are visiting",location['description'])
                
                for i in range(5):
                    Player.bag.add_item(PokeBall("Ultra Ball"))
                    Player.bag.add_item(Potion("Potion"))
                    Player.bag.add_item(Revive("Revive"))
                    Player.bag.add_item(RazzBerry("Razz Berry"))
    
    else:
                print("There's something wrong with entered location ! Please Try again!\n")
            

### Function to return the values for Pokestop locations
def getPokestop():
    print (" **** Following are the Pokestop locations around you ****")
    request_str = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Massachusetts&types=(cities)&key=AIzaSyAyoWh3bL8Odto5oXOG00Hw2qAT96MwMkk"
    
    #Getting response
    
    response=requests.get(request_str)
    num_of_stops=len(response.json()['predictions'])
    
    if(num_of_stops>0):
        print("Select a place to visit:\n")
        for i in range(num_of_stops):
            print(i+1,":",response.json()['predictions'][i]['description'])