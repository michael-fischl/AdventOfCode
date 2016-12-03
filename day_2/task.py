code = ""
pad = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
x = 1
y = 1
with open('input', 'r') as f:
    for line in f:
        for char in line:
            if (char == 'U'): y = 0 if y == 0 else y - 1
            if (char == 'D'): y = 2 if y == 2 else y + 1
            if (char == 'L'): x = 0 if x == 0 else x - 1
            if (char == 'R'): x = 2 if x == 2 else x + 1
        code += str(pad[y][x])
    print "The code is " + code + "!"
