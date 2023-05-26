import tkinter as tk
from tkinter import messagebox

# LIAM Program

# DISCLAIMER: 
# The LIAM program is a personal project and is provided for educational and entertainment purposes only. 
# The information and suggestions provided by LIAM are based on general knowledge and should not be considered as professional advice.
# The creator of LIAM and OpenAI, the developers of the underlying AI technology, cannot be held responsible for any actions taken or decisions made based on the suggestions or information provided by LIAM.
# Users of the LIAM program are solely responsible for their own actions and should exercise caution and judgment when interpreting and implementing the suggestions and information provided.

def safe_mode():
    # Add code for safe mode operations here
    messagebox.showinfo("Safe Mode", "Safe mode is activated.")

def main():
    # Welcome pop-up window
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Welcome", "Welcome to LIAM!")
    root.destroy()

    while True:
        user_input = input("Enter your command: ")

        if user_input == "safe":
            safe_mode()
        
        # Add other commands and functions here
        
        else:
            print("Invalid command. Please try again.")

# Execute the LIAM program
if __name__ == "__main__":
    main()
