def posLetra(phrase, letter, pos):
    occurance = 0
    i = 0
    while i < len(phrase):
        if letter == phrase[i]:
            occurance += 1
            if occurance == pos:
                return i
        i += 1
    if occurance < pos:
        return -1