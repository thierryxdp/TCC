def lingua_p(palavra):
    p = palavra.lower()
    i = 0
    l = []
    for i in range(len(palavra)):
        if p[i] != "a" and p[i] != "e" and p[i] != "i" and p[i] != "o" and p[i] != "u":
            list.append(l, p[i])
        else:
            list.append(l, p[i]+"p"+p[i])
    return "".join(l)