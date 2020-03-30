import sys
file_name = sys.argv[1]
number_of_lines = None
count = 0
write = []
current_line = ''
number = open(file_name, 'r')
while number_of_lines != '':
    number_of_lines = number.readline()
    count += 1
for i in range(count):
    append_list = number.readline()
    write.append(append_list)
number.close()
append = open(file_name, 'w')
for i in range(count):
    current_line = write[i]
    append.write('Lior ')
    append.write(current_line)
    append.write(' Rozenblit\n')
append.close()
readFile = open(file_name, 'r')
md = readFile.read()
print(md)
print(write)
