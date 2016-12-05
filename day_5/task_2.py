import hashlib

with open('input', 'r') as f:
    for line in f:
        found = 0
        integer = 0
        password = ['_']*8
        while found < 8:
            to_hash = line + str(integer)
            m = hashlib.md5()
            m.update(to_hash)
            hash = str(m.hexdigest())
            if hash.startswith("00000"):
                position = int(hash[5]) if hash[5].isdigit() else -1
                if position >= 0 and position <= 7:
                    if password[position] == '_':
                        password[position] = hash[6]
                        found += 1
            integer += 1
        print "The password is " + ''.join(password) + "!"
