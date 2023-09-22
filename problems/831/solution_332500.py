def lingua_p(palavra):
    i = 0
    palavra2 = []
    while i < len(palavra):
        if palavra[i] in "aeiouAEIOUáâãéêíóôú":
            list.append(palavra2, palavra[i] + 'p' + palavra[i])
        else:
            list.append(palavra2, palavra[i])
        i = i + 1
    return str.join('',palavra2)