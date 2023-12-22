def print_matrix_integer(matrix=[[]]):
        for row in matrix:
            for i, element in enumerate(row):
            # Use str.format() to print integers without casting them into strings
                if i == len(row) - 1:
                # Print without trailing space for the last element in a row
                     print("{:d}".format(element), end="")
                else:
                     print("{:d} ".format(element), end="")
            print()