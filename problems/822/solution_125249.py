def repetidos(lista):
    elemento = str(lista[0])
    i = 0
    s = 0
    while i < len(elemento):
        if int(elemento[i - 1]) == int(elemento[i]):
            s = s + 1
        	i = i + 1
        else:
            s = s
        	i = i + 1
    return s