triangle = [[1], [1, 1]]

def pascal(n):
    if n < 1:
        print('NO')
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            prev_row = triangle[row_number - 1]
            length = len(prev_row) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    value = triangle[row_number - 1][i - 1] + triangle[row_number - 1][i]
                    row.append()
                else: 
                    row.append(1)
            triangle.append(row)
            row_number += 1
        
        for row in triangle:
            print(row)

pascal(2)