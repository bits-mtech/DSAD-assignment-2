def process_line_record(str):
    '''
    This is helper function to process line information from input and prompts file.
    :param str: Line content
    :return: <Array>
    '''
    return [input.rstrip(" ").lstrip(" ") for input in str.strip("\n").split("/") if
                                       len(input) > 0]

def readFromInputFile(filename="inputPS6.txt"):
    '''
    Read the content of file.
    :param filename:
    :return: <None>
    '''
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        print_to_output = ""
        if filename == "inputPS6.txt":
            for line in lines:
                processed_array = process_line_record(line)
                print_to_output = print_to_output + processed_array.pop() + '\n'
            writeToOutputFile(print_to_output)

def writeToOutputFile(str,operation="input" ,filename="outputPS6.txt"):
    '''
    This function write output of the program into supplied filename parameter.
    :param str: Content needs to be written in output file
    :param operation: Mode of operations like insert,update,status check, member refernce check.
    :param filename: Output filename default value is outputPS6.txt
    :return: <None>
    '''
    with open(filename, 'a+') as fh:
        if operation == 'input':
            fh.write(f'{str}')


if __name__ == '__main__':
    readFromInputFile()