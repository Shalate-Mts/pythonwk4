#reading the file and printing it's contents
try:
    #reading existing file
    existingfile = input("What is the name of the file you're trying to open (.txt): ")
    with open(existingfile, "r") as file:
        old_data = file.read()
        print(old_data) 
#creating and writing a new file
    newfile = input("enter the name of your new file (.txt): ")
    new_data = input("share the content you want to add to file (.txt): ")
    with open(newfile, 'w') as file:
        modfile = new_data + '\n' + old_data
        file.write(modfile)
    print(f"created successfully {modfile}")
except FileNotFoundError: 
    print("file not found/error")