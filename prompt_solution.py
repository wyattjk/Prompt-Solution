## Wyatt Kirisits - 1/31/22
## This is my application for the Engineering Intership at Sports Reference
## This program displays a matrix of head to head records, given a json file
## that includes each team's Win-Loss records versus opponents

#import json package to work with json file
import json

from tabulate import tabulate

#opens json file
file = open('head.json')

#defines a dictionary using contents of json file
dictionary = json.load(file)

#define list for table values
finList = []

#define a list for the first row in the table
labels = ['Tm']

#for loop to input team abbreviations into the labels list
for name in dictionary:
    labels.append(name)

#define iteration variable for the following nested for loop
i = 1
#for loop to iterate through dictionary
for name in dictionary:

    #define an empty temporary list 
    tempList = []
    
    #append team name to the temporary list
    tempList.append(name)
    
    #define new variable for ease of coding
    team = dictionary[name]

    #for loop to iterate through each team's opponents
    for opp in team:
        
        #append team's number of wins vs each opponent to the temporary list
        tempList.append(team[opp]['W'])

    #inserts a '--' into the temporary list to prevent confusion (a team cannot play itself)
    tempList.insert(i, '--')
    #increase iteration variable
    i = i + 1
    #append the temporary list to the final list of table values
    finList.append(tempList)

#displays final list
print(tabulate(finList, headers=labels, tablefmt="fancy_grid"))

#closes json file 
file.close()

