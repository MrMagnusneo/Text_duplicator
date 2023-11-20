def restart_program():
    # Ask user if they want to restart
    restart = input("Restart? Y/N => ").lower()

    # Check user's response
    if restart == "y":
        # If 'y', return True to indicate restart
        return True
    elif restart == "n":
        # If 'n', print a message and return False to indicate stopping
        print("Program will be stopped.")
        return False
    else:
        # If an unknown answer is given, print an error and recursively call restart_program
        print("Error, unknown answer.")
        return restart_program()

def main():
    while True:
        # Welcome message
        print("Welcome to the text duplicator. Thank you for using it. Follow the steps to use it")

        # Get user input for count
        count = input("Input count: ")

        # Check if the input is a digit
        if not count.isdigit():
            # If not a digit, print an error and restart the program
            print("Error, not a digit.")
            restart = restart_program()
            if not restart:
                break
            else:
                continue

        # Convert count to an integer
        count = int(count)

        # Get user input for text
        text = input("Input text: ")
        print("Select output mode")

        # Get user input for mode
        mode = input("Input [p] for output text in line or [ln] for outputting text on a new line => ")

        # Check user's mode choice
        if mode == "p":
            # If 'p', get user input for separator and print the duplicated text
            separator = input("Input separate symbol: ")
            print((text + separator) * count)
        elif mode == "ln":
            # If 'ln', print the text on new lines using a for loop
            for _ in range(count):
                print(text)
        else:
            # If an unknown mode is selected, print an error and restart the program
            print("Error, incorrect mode.")
            restart = restart_program()
            if not restart:
                break
            else:
                continue

        # Ask user if they want to restart the program
        restart = restart_program()
        if not restart:
            break

if __name__ == "__main__":
    # Start the main function if the script is run
    main()
