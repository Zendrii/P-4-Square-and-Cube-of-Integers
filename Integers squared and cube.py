# read external file
with open('integers.txt', 'r') as main_file, open('double.txt', 'w') as squared_file, open('triple.txt', 'w') as cubic_file:
    for line in main_file:
        integers = int(line)
        # check for even integers
        if integers % 2 == 0:
            even_nmbrs = str(integers)
            # square the even integers
            
            # create separate text file for squared integers
            # check for odd integers
            # cube the odd integers
            # create separate text file for cubic integers