def square_matrix_simple(matrix=[]):
    new_matrix=[[0 for i in range(len(matrix[i]))] for  i in range(len(matrix))]
        # Iterate through each element of the input matrix and square the values
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2


    return new_matrix