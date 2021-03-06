with open('input', 'r') as f:
    input = f.read().replace(", ", "")
    orientation = 0
    position_x = 0
    position_y = 0

    c = 0
    while c < len(input):
        if (input[c] == 'R'):
            orientation = 0 if (orientation == 3) else orientation + 1
            c += 1
            continue
        if (input[c] == 'L'):
            orientation = 3 if (orientation == 0) else orientation - 1
            c += 1
            continue
        length = ""
        while (c < len(input) and input[c] != 'L' and input[c] != 'R'):
            length += input[c]
            c += 1
        if (orientation == 0): position_y += int(length)
        if (orientation == 1): position_x += int(length)
        if (orientation == 2): position_y -= int(length)
        if (orientation == 3): position_x -= int(length)
    print "It is " + str(abs(abs(position_x) + abs(position_y))) + " blocks away!"
