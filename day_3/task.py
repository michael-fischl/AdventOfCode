valid = 0
with open('input', 'r') as f:
    for line in f:
        triangle = [int(s) for s in line.split() if s.isdigit()]
        first = triangle[0] < (triangle[1] + triangle[2])
        second = triangle[1] < (triangle[0] + triangle[2])
        third = triangle[2] < (triangle[1] + triangle[0])
        if first and second and third: valid += 1
    print str(valid) + " triangles are valid!"