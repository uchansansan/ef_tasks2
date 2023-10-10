with open("input.txt", "r") as file_in, open("output.txt", "w") as file_out:
    for line in file_in:
        if line[0] == "A" or line[0] == "a":
            file_out.write(line)
