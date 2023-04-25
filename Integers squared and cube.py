# read external file
with open('integers.txt', 'r') as main_file, open('double.txt', 'w') as squared_file, open('triple.txt', 'w') as cubic_file:
    for line in main_file:
        integers = int(line)
        # check for even integers
        if integers % 2 == 0:
            # square the even integers
            square = pow(integers, 2)
            even_nmbrs = str(square)
            # create separate text file for squared integers
            squared_file.write(even_nmbrs + '\n')
        # check for odd integers
        else:
            # cube the odd integers
            cube = pow(integers, 3)
            odd_nmbrs = str(cube)
            # create separate text file for cubic integers
            cubic_file.write(odd_nmbrs + '\n')