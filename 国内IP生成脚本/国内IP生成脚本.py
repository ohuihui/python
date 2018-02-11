import math

str_file_input = 'delegated-apnic-latest.txt'
str_file_output = 'cnip.txt'


def __main():
    f_input = open(str_file_input, 'r')
    f_output = open(str_file_output, 'w')
    filtered_lines = [line.split('|')
                      for line in f_input if('CN|ipv4' in line)]
    for line in filtered_lines:
        #ip = 'address ' + line[3] + ' mask ' + \
        #    str(32 - int(math.log2(int(line[4]))))
        ip = line[3]
        f_output.write(ip + '\n')
        print(ip + '\n')

    f_input.close()
    f_output.close()


if __name__ == '__main__':
    __main()
