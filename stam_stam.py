import sys
file_name = sys.argv[1]
file_name2 = sys.argv[2]
number_of_lines = None
count = 0
write = []
current_line = ''
number = open(file_name, 'r')
while number_of_lines != '':
    number_of_lines = number.readline()
    count += 1
number.close()
number1 = open(file_name, 'r')
for i in range(count):
    append_list = number1.readline()
    write.append(append_list)
number1.close()
append = open(file_name2, 'w')
for i in range(1, count):
    current_line = write[i-1]
    append.write('Lior ' + current_line.strip('\n') + ' Rozenblit\n')
append.close()
readFile = open(file_name2, 'r')
PrintFile = readFile.read()
print(PrintFile)