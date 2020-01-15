filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

matrix = [[0 for i in range(1000)] for j in range(1000)]

# overlap_count = 0

for line in lines:
    left, right = line.split(': ')
    id, inches = left.split('@ ')
    y, x = inches.split(',')
    y = int(y)
    x = int(x)
    y_len, x_len = right.split('x')
    y_len = int(y_len)
    x_len = int(x_len)

    # for i in range(x, x + x_len):
    #     for j in range(y, y + y_len):
    #         if matrix[i][j] == 0:
    #             matrix[i][j] = 1
    #         elif matrix[i][j] == 1:
    #             overlap_count += 1

# print(overlap_count)

    for i in range(x, x + x_len):
        for j in range(y, y + y_len):
            matrix[i][j] += 1
  
count = 0

for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 1:
                count += 1

print(count)



