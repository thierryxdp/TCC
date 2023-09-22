def repetidos(l):
    a = -1
    i = 0
    resultado = 0
    while i < len(l):
        if l[i] == l[a]:
        	resultado = resultado + 1
        a = a + 1
        i = i + 1
    return resultado