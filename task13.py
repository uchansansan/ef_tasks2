input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

word_frequency = {}

for line in input_file:
    words = line.split()
    for word in words:
        word = word.strip().lower()
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

input_file.close()

sorted_words = sorted(word_frequency.items())

for word, frequency in sorted_words:
    output_file.write(f'{word}: {frequency}\n')

output_file.close()
