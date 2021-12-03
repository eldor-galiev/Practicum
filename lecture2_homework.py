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
a = [[1111,22,333],[4,555,6],[777,8888,999]]
print_matrix_modified(a)