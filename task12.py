output_file = open('index.html', 'w')

output_file.write('<!DOCTYPE html>\n')
output_file.write('<html>\n')
output_file.write('<head>\n')

input_file = open('input.txt', 'r')
lines = input_file.readlines()
input_file.close()

output_file.write(f'<title>{lines[0]}</title>\n')
output_file.write('</head>\n')
output_file.write('<body>\n')
output_file.write('<h1>' + lines[1].strip() + '</h1>\n')

for line in lines[2:]:
    output_file.write('<p>' + line.strip() + '</p>\n')

output_file.write('</body>\n')
output_file.write('</html>\n')

output_file.close()
