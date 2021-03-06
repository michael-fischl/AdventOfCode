with open('input', 'r') as f:
    sum = 0
    for line in f:
        room = line.split("[")[0].replace("-", "")
        check = line.split("[")[1].replace("]", "").replace("\n", "")
        sector = ""
        for c in reversed(room):
            if c.isdigit():
                sector += c
                continue
            break
        sector = sector[::-1]
        room = room.replace(sector, "")

        room_sorted = ''.join(sorted(room))
        char = 0
        last = ''
        count = 0
        list = []
        while char < len(room_sorted):
            if last == '':
                count += 1
                last = room_sorted[char]
                char += 1
                continue
            if last == room_sorted[char]:
                count +=1
                char +=1
                continue
            list.append((last, count))
            count = 1
            last = room_sorted[char]
            char += 1
        list.append((last, count))
        list.sort(key=lambda tup: tup[1], reverse=True)
        checksum = ""
        for i in range(0, 5):
            checksum += list[i][0]

        if checksum == check:
            sum += int(sector)
    print "The sum of valid sectors is " + str(sum) + "!"
