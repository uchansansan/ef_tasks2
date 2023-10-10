with open("input.txt", "r") as file_in, open("output.txt", "w") as file_out:
    file_out.write(file_in.read().upper())
