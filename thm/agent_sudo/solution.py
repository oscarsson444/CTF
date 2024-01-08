
# Create a new file with usernames of length 5 to use with ffuf

with open('new_usernames.txt', 'w') as new_file:
    with open('usernames.txt', 'r') as file:

        for line in file:
            print(line)
            if line[0] == "R" or line[0] == "r":
                new_file.write(line)
            else:
                continue