print ("Welcome to the text duplicator. Thank you for using it. Follow the steps to use it")
while True:
    count = input("input count: ")
    if count.isdigit():
        count = int(count)
        text = input("input text: ")
        print ("select output mode")
        mode = input("input [p] for output text in line or [ln] for outputting text on new line => ")
        if mode == "p":
            separator = input("input separate symbol: ")
            print ((text + separator) * count)
        elif mode == "ln":
            while count > 0:
                print (text)
                count -= 1
        else:
            print ("error, incorrect mode")
            r = input ("restart? Y/N => ")
            if r[0] == "Y" or r[0] == "y":
                continue
            elif r[0] == "N" or r[0] == "n":
                break
            else:
                print ("error, unknown answer")
                print ("program will be stopped")
                break

    else:
        print ("error, not digit")
        r = input ("restart? Y/N => ")
        if r[0] == "Y" or r[0] == "y":
            continue
        elif r[0] == "N" or r[0] == "n":
            break
        else:
            print ("error, unknown answer")
            print ("program will be stopped")
            break
    r = input ("program completed, restart? Y/N => ")
    if r[0] == "Y" or r[0] == "y":
        continue
    elif r[0] == "N" or r[0] == "n":
        break
    print ("error, unknown answer")
    print ("program will be stopped")
    break
