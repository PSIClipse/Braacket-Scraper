#Scraping data from Braacket.com for ease of use

#importing libraries that will be used during this session
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


#constant variables that shouldnt be changed unless stated otherwise
index = 0
FinalData = ['Player Name', 'Placement', 'Total Matches', 'Wins', 'Draws', 'Losses', 'Win Rate', 'Score For', 'Score Against', 'Score Difference']
#creates a data frame using panda with the correct information that relates to the data we will scrape from braacket.com
df = pd.DataFrame(columns = FinalData)
#user input's the bracket they would like to retrieve data from
Choice = int(input('Please type "1" if you would like the CHECK_IN LIST, or type "2" if you would like the TOURNAMENT_RANKING, or type "3" if you would like to read the ABOUT_SECTION :'))
#######################################################################################################################################################


if Choice == 1:
  #(changed to string as the input is currently a float or int)
  BracketVR = str(input("What Mid-Week Mixup Bracket are you up to?  :"))
  #allows user to either type in a Folder to place files in every time or allow user to write Folder into code directly
  FileType = input("Please paste location you would like the file to be Placed.  : ")
  #FileType = 'PLEASE REPLACE THIS TEXT WITH YOUR FOLDER LOCATION AND UNCOMMENT, THEN COMMENT THE ABOVE CODE'

    
  #using the BracketVR, the program is able to swap out the bracket number in the url, doesnt need to be changed to an string as it has been done above
  URL1 = ('https://braacket.com/tournament/midweekmixup'+BracketVR+'/player')
  #using the request library, we are able to grab the html of the page and store it as a variable
  page1 = requests.get(URL1)
  #using the BS4 library, we are able to display the snapshot of the website we took and display it as a html file in the console
  soup1 = BeautifulSoup(page1.text, 'html')
  
  #using the BS4 library and inspect element, we are able to sort through the html and find the exact data we need from the website
  #td being used to find the data and class_ to sort through the data for just the names we need
  HTMLPlayers = soup1.find_all('td', class_= 'ellipsis')
  #this had taken 2 1/2 hours to fix, and i still dont understand what had gone wrong where i couldnt strip the html from the list i made
  #Player_names is the html taken away from the data that i have scrubbed from the braaket website 
  Player_Names = [Player.text.strip() for Player in HTMLPlayers]
  print(Player_Names)
  df = pd.DataFrame(Player_Names)
  df.to_csv(FileType + '\\' + 'MidWeek_MixUp_CHECK-IN.csv', index=False)


elif Choice == 2:
  #(changed to string as the input is currently a float or int)
  BracketVR = str(input("What Mid-Week Mixup Bracket are you up to?  :"))
  #allows user to either type in a Folder to place files in every time or allow user to write Folder into code directly
  FileType = input("Please paste location you would like the file to be Placed.  : ")
  #FileType = 'PLEASE REPLACE THIS TEXT WITH YOUR FOLDER LOCATION AND UNCOMMENT, THEN COMMENT THE ABOVE CODE'
  
    
  #using the BracketVR, the program is able to swap out the bracket number in the url, doesnt need to be changed to an string as it has been done above
  URL1 = ('https://braacket.com/tournament/midweekmixup'+BracketVR+'/player')
  #using the request library, we are able to grab the html of the page and store it as a variable
  page1 = requests.get(URL1)
  #using the BS4 library, we are able to display the snapshot of the website we took and display it as a html file in the console
  soup1 = BeautifulSoup(page1.text, 'html')
  #using the BracketVR, the program is able to swap out the bracket number in the url, doesnt need to be changed to an string as it has been done above
  URL2 = ('https://braacket.com/tournament/midweekmixup'+BracketVR+'/ranking')
  #using the request library, we are able to grab the html of the page and store it as a variable
  page2 = requests.get(URL2)
  #using the BS4 library, we are able to display the snapshot of the website we took and display it as a html file in the console 
  soup2 = BeautifulSoup(page2.text, 'html')
  

  #using the BS4 library and inspect element, we are able to sort through the html and find the exact data we need from the website
  #td being used to find the data and class_ to sort through the data for just the names we need
  HTMLPlayers = soup1.find_all('td', class_= 'ellipsis')
  #this had taken 2 1/2 hours to fix, and i still dont understand what had gone wrong where i couldnt strip the html from the list i made
  #Player_names is the html taken away from the data that i have scrubbed from the braaket website 
  Player_Names = [Player.text.strip() for Player in HTMLPlayers]
  #using a second BS4 we are able to grab the player ranking and data for that player into a second list to be manipulated
  HTMLRanking = soup2.find_all('td', class_='text-center')
  HTMLPlayersInOrder =soup2.find_all('td', class_= 'ellipsis')
  #PlayerRanking and PlayersInOrder are ran throught the FOR Loop and have their HTML striped away from them
  PlayerRanking = [Ranking.text.strip() for Ranking in HTMLRanking]
  PlayersInOrder = [Order.text.strip() for Order in HTMLPlayersInOrder]
  #using the BS4 library and inspect element, we are able to sort through the html and find the exact data we need from the website
  #td being used to find the data and class_ to sort through the data for just the names we need
  HTMLPlayers = soup1.find_all('td', class_= 'ellipsis')
  #this had taken 2 1/2 hours to fix, and i still dont understand what had gone wrong where i couldnt strip the html from the list i made
  #Player_names is the html taken away from the data that i have scrubbed from the braaket website 
  print(PlayersInOrder)
  

  #using numpy we are able to split the list by the number of people in the list itself, which was WAY easier then spliting the list by 9 since it means the exact same thing
  PlayerRankingButBetter = np.array(PlayerRanking)
  PlayerRankingSplit = np.split(PlayerRankingButBetter, len(PlayersInOrder)) 
  #converts the numpy split into something we can actually work with lmao
  PlayerRankingSplitIntoList = np.array(PlayerRankingSplit).tolist()
  

  #PlayerRankingSplitIntoList[0].insert(0,PlayersInOrder[0])
  #a representation of what i need to do with the list in order to insert each player into their respective spot in the matrix
  #NOTE while using a while loop i insert each player into the start of each matrix while also adding them to the data frame one spot at a time
  while index != len(PlayersInOrder):
      PlayerRankingSplitIntoList[index].insert(0,PlayersInOrder[index])
      df.loc[len(df)] = PlayerRankingSplitIntoList[index]
      index += 1
  PlayerRankingSplitIntoList
  #must add \\ instead of \ becasue python reasons.
  df.to_csv(FileType + '\\' + 'MidWeek_MixUp_Ranking.csv', index=False)


elif Choice == 3:
    print("Hello, If you are reading this, it means you entered 3 on your keyboard :D")
    print("But seriously, thank you for using PSIClipse's (or in Matthew's) first real program")
    print("This code was offically completed 25 days after the day Matthew had first learned how to use Python")
    print("Please feel free to MSG me if there are any bugs in the script (lord knows where)")


else:
    print("Error, Please don't disobey the code :(")

