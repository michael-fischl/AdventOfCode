valid = 0
cols = []
cols.append([])
cols.append([])
cols.append([])

with open('input', 'r') as f:
    for line in f:
        triangle = [int(s) for s in line.split() if s.isdigit()]
        cols[0].append(triangle[0])
        cols[1].append(triangle[1])
        cols[2].append(triangle[2])
    for col in range(len(cols)):
        i = 0
        while i < len(cols[col]):
            triangle = [cols[col][i], cols[col][i + 1], cols[col][i + 2]]
            first = triangle[0] < (triangle[1] + triangle[2])
            second = triangle[1] < (triangle[0] + triangle[2])
            third = triangle[2] < (triangle[1] + triangle[0])
            if first and second and third: valid += 1
            i += 3
    print str(valid) + " triangles are valid!"