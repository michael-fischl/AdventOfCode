import operator

with open('input', 'r') as f:
    message_length = len(f.readline()) - 1
    f.seek(0)
    occurences = [dict() for x in range(message_length)]
    print message_length
    for line in f:
        for i in range(message_length):
            if occurences[i].has_key(line[i]):
                occurences[i][line[i]] += 1
            else:
                occurences[i][line[i]] = 1
    message = ""
    for i in range(message_length):
        message += min(occurences[i].iteritems(), key=operator.itemgetter(1))[0]
    print "The message is " + message + "!"