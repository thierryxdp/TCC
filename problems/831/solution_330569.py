def lingua_p(palavra):
    newstring = "".join(["{0}p{0}".format(letter) if letter.lower() in "aeiou" else letter for letter in palavra])
    return newstring