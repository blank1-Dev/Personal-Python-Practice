# Simple Names Program
# By blank1-Dev
# Practicing with classes, functions, and if statements

class Names:
    name_list = ['John', 'Kelly'] # The names
    
    def add_name(self, name): # Function that appends the users given name to the list
        self.name_list.append(name)
        return self.name_list
        
def name_prompt(): # Executed first before Names class. Gets input from user.
    name_class = Names() # Mentions the class
    ask = input("Add Name or type 'quit': ") # Waits for input under the function "ask"
    name_class.add_name(ask) # Passes the name through variable "name" in "add_name"
    if ask == "quit":
        quit() # Quit the program when user types "quit"
    else:
        print(name_class.name_list) # Else, print the names list in the Names class
        restart() # Call the restart function
def restart():
    name_prompt() # Restarts name_prompt()

name_prompt() # allows the program to ask for input right away.

