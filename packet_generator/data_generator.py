
#This function creates data for the network segments from user input.
def data_generator(text):

    # This section prompts the user for their message
    # message = input("What is your message?:\n\n")

    #Creates a container for the output of this function
    binary_list = []

    for char in text:
        # This code changes each character from the input to a number from ASCII
        # then changes that ASCII number to binary_list
        # then appends that binary to binary_list
        binary_list.append(bin(ord(char)))

    # print(binary_list)
    # print("\n\n")

    return(binary_list)
