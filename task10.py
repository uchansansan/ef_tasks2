import os

directory = 'simple'
if not os.path.exists(directory):
    os.makedirs(directory)

input_file = open('input.txt', 'r')
data = input_file.readlines()
input_file.close()

even_lines = [line for index, line in enumerate(data) if index % 2 == 1]

output_file = open('simple/output.txt', 'w')
output_file.writelines(even_lines)
output_file.close()
