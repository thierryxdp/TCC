def uppCons(string):
    x = ""
    for letter in string:
        if letter not in "aeiouAEIOU":
            x = x + letter.upper()
        else:
            x = x + letter.lower()
    return x