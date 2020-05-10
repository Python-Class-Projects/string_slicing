'''
Write a program that will ask for the user to enter a phrase. We will then retrieve that phrase and ask the user for starting
and end positions. These starting and end positons will be the start and end positions of the string to print. 
The program will be inside of a loop to constantly ask the user if he/she wants to play again. 
'''

# Function to loop over the game. Retrieving input, outputting during the game.
def phrase_loop(play_again,phrase):

	while play_again == "y":
		start_end = input("Enter starting and ending position numbers: ")
		split_start_end = start_end.split(" ")
		split_start = int(split_start_end[0])
		split_end = int(split_start_end[1])
		sliced_phrase = phrase[split_start:split_end]
		error_catcher(split_start, split_end, sliced_phrase) #Calling error_catcher function to determine if error.
		play_again = input("Again? ")
		play_again = play_again.lower()

	return split_start, split_end, sliced_phrase

#Function used to determine if the user entered incorrect values.
#If entered incorrectly, error message comes up. If entered correctly, the output is shown of the sliced string.
def error_catcher(split_start, split_end, sliced_phrase):
	if(split_start > split_end):
		print("Invalid. The starting position must be less than the ending position.")
	else: 
		print(f"That slice is '{sliced_phrase}'.")


#Main 
phrase = input("Enter a phrase: ")
print("Thank you. Now we'll crave it up.")
play_again = "y"
phrase_loop(play_again,phrase)
print("\nEND OF PROGRAM.\n")
