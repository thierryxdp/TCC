def posLetra(s,l,o):
    i = 0
    vezes = 0
    while i < len(s):
        if s[i] == l:
            vezes = vezes + 1
            if vezes == o:
                return i
            elif vezes < o:
                return -1
        i = i+1