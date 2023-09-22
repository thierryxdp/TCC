def posLetra(s,l,o):
    i = 0
    vezes = 0
    while i < len(s):
        if s[i] == l:
            vezes = vezes + 1
        elif s[i] == l and vezes == o:
            return ocorrencia
        elif vezes < o:
            return -1
        i = i + 1