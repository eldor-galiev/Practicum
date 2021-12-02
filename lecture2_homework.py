def get_max_size_in_column(B, idx):
    max_num = -float("inf")
    for row in B:
        max_num=max((row[idx]),max_num)
    return len(str(max_num))

def print_matrix_modified(matrix):
    column_number = len(matrix[0])
    for row in matrix:
        row_str = ""
        for index in range(column_number):
            row_str += str(row[index]).rjust(get_max_size_in_column(matrix,index)+1) + " "
        print(row_str)
a = [[12121,1,141],[5,224444443,4],[12,232,2134]]
print(print_matrix_modified(a))
