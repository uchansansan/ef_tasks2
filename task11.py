input_file = open('input.txt', 'r')
numbers = [int(line.strip()) for line in input_file]
input_file.close()

numbers.sort(reverse=True)

output_file = open('output.txt', 'w')
for number in numbers:
    output_file.write(str(number) + '\n')

output_file.close()
