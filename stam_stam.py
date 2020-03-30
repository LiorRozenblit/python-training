import sys
FileNameRead = sys.argv[1]
FileNameWrite = sys.argv[2]
Count = 0
Write = []
CurrentLine = ''
def change_list(Count):
    number = open(FileNameRead, 'r')
    for line in number:
        Count += 1
    number.close()
    number1 = open(FileNameRead, 'r')
    for i in range(Count):
       append_list = number1.readline()
       Write.append(append_list)
    number1.close()


def change_file(Count,):
    append = open(FileNameWrite, 'w')
    for i in range(1, Count):
        CurrentLine = Write[i-1]
        append.write('Lior ' + CurrentLine.strip('\n') + ' Rozenblit\n')
    append.close()


def main():
    change_list(Count)
    change_file(Count)
    readFile = open(FileNameWrite, 'r')
    print_new_file = readFile.read()
    print(print_new_file)


if __name__ == '__main__':
    main()