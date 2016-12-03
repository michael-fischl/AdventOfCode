code = ""
pad = [['_', '_', '1', '_', '_'],
       ['_', '2', '3', '4', '_'],
       ['5', '6', '7', '8', '9'],
       ['_', 'A', 'B', 'C', '_'],
       ['_', '_', 'D', '_', '_']]
x = 0
y = 2
with open('input', 'r') as f:
    for line in f:
        for char in line:
            if (char == 'U'):
                y -= 1
                if y == -1: y = 0
                if pad[y][x] == '_': y += 1
            if (char == 'D'):
                y += 1
                if y == 5: y = 4
                if pad[y][x] == '_': y -= 1
            if (char == 'L'):
                x -= 1
                if x == -1: x = 0
                if pad[y][x] == '_': x += 1
            if (char == 'R'):
                x += 1
                if x == 5: x = 4
                if pad[y][x] == '_': x -= 1
        code += str(pad[y][x])
    print "The code is " + code + "!"
