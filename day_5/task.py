import hashlib

with open('input', 'r') as f:
    for line in f:
        found = 0
        integer = 0
        password = ""
        while found < 8:
            to_hash = line + str(integer)
            m = hashlib.md5()
            m.update(to_hash)
            hash = str(m.hexdigest())
            if hash.startswith("00000"):
                password += hash[5]
                found += 1
            integer += 1
        print "The password is " + password + "!"
