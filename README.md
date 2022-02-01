# Prompt-Solution
This README.md file provides an explanation to my solution.

First, I copied and pasted the provided json data into a blank notebook on the notepad application. 
Next, I saved that file as a .json file called "head.json" to the same folder that I run python on my computer, as I am using the python language to solve this prompt.
For the actual code solution, I started off by opening the json file and assigning it to a variable using the open() method. I noticed that the file was essentially a dictionary of dictionaries, where each element in the dictionary (team name abbreviation) was assigned to a dictionary (each element in these secondary dictionaries is the team's opponent's name abbreviation and the amount of wins and losses accrued against that opponent.)
To create the matrix of head to head records, I created a nested for loop to get the information from the dictionaries (each team, their opponents, and their record against that opponent) and then input that data into a temporary list called "tempList" that consisted of only the team name and their amount of wins versus each opponent.
As a team does not ever compete against itself, the cells in the matrix that contained data on a team's head to head record against itself must be blank. I used the insert() method on python to insert a "--" at the correct index in the list, so that the final matrix would have "--" in the correct cells. 
Then, I appended this temporary list to a final list of lists, called "finList". This final list contained lists that contained each team name and their total wins versus each opponent. 
For the headers of the table, I used a for loop to get each element of the main dictionary and append that to a list called "labels" which was initially defined as a list with only one element: "Tm"
Then, I utilized the tabulate library within python to create a visually appealing table. That is, a matrix of head to head records. I used the list "finList" for the rows, and the list "labels" for the headers. In addition, I used the tablefmt argument to make the table easier to comprehend.
Finally, I closed the json file with a .close command.
