def uppCons(string):
    x = ""
    for letter in phrase:
        if letter not in "aeiouAEIOU":
            x = x + letter.upper()
        else:
            x = x + letter.lower()
    return x