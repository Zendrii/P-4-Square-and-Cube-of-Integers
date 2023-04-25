# read external file
with open('integers.txt', 'r') as main_file, open('double.txt', 'w') as squared_file, open('triple.txt', 'w') as cubic_file:
    for line in main_file:
        integers = int(line)
        # check for even integers
        if integers % 2 == 0:
            even_nmbrs = str(integers)
            # square the even integers
            square = even_nmbrs ** 2
            # create separate text file for squared integers
            squared_file.write(square + '\n')
            # check for odd integers
            # cube the odd integers
            # create separate text file for cubic integers