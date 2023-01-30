"""
Name: Drew Cochran
Date: 24JAN2023
Description: Script file to create and store a list of household items and those items value in a text file that can be
read by the user. Also, additional items can be stored in the text file once the program is run again.
Changelog:
    26JAN2023: Writing new functions to call for opening document and apending the document.
    27JAN2023: Corrected "None" error; program was displaying word "None" due to using input() with embedded print()
    function. Oops.
    30JAN2023: Opened to take screenshots for assignment learning document. No changes.

"""

# Function to start and open the text file

def HouseHoldItemTxtFile():

    # Establish variables

    HouseHoldItems = open('C:\\_PythonClass\\Assignment03\\HouseHoldItemsAndValue.txt', mode='a')
    Items = ''
    Value = ''

    # while loop to keep program running until user enters "Exit"
    while(True):

        # Items is the primary variable, determines if user is entering new household item or wants to end the program
        Items = input("Enter an Item (Or type 'Exit' to quit): ")

        # If statement to determine if user wants to end program
        if(Items.lower() == "exit"):
            break

        # Else statement to write household items to the file, followed by value of items
        else:
            HouseHoldItems.write(Items + ', ')
            Value = input("Enter an estimated Value: ")
            HouseHoldItems.write(Value + '\n')

    HouseHoldItems.close()

HouseHoldItemTxtFile()