def posLetra (string, letra, n):
    a = 0
    contador = 0
    while a < len(string)-1:
        if string[a] == letra:
            contador +=1
        if contador == n:
            return a
        a +=1
    return -1