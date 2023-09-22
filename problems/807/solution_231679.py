def conta_frases(texto):
    i = 0
    count = 0
    while i < len(texto):
        if texto[i] == '.':
            if i+2 < len(texto):
                if texto[i+1] == '.' and texto[i+2] == '.':
                    i += 2
            count += 1
        elif texto[i] == '!' or texto[i] == '?':
            count += 1
        i += 1
    return count