with open("input.txt", "r") as file_in, open("output.txt", "w") as file_out:
    characters = [line.strip()[-1] for line in file_in]
    sequence = "".join(characters)
    file_out.write(sequence)
