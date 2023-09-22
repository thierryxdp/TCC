def changeCaps(string):
    for c in string:
        if c.islower():
            print(c.upper())
        else:
            print(c.lower())