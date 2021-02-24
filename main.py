def calculate_balanced_dish(str):
    '''
    This function is used to calculate the balanced dish count based on
    supplied menu. example if supplied string value is SPSSPP the output should be 2
    :return: <int> Output of balanced dish
    '''
    arr = [char for char in str]  #Convert the string into charcter array
    counter = 0
    item_count = len(arr)
    balanced_dish = 0

    # Loop through length of character array and check is adjacent elements are same,
    # pop them from array and increment the balanced dish count
    while counter < item_count:
        if (counter > 0 and arr[counter] != arr[counter - 1]):
            for c in range(0, counter):
                arr.pop(0)
                arr.pop(0)
            item_count = len(arr)
            balanced_dish += 1
            counter = 0
        counter += 1
    return balanced_dish

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
                print_to_output = print_to_output + str(calculate_balanced_dish(processed_array[0])) + '\n'
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