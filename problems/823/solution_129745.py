# Questão OBI

def faltante(lista):
    lista.sort()
    i=1
    if lista[0] != 1:
        return 1
    while i < len(lista):
        if lista[i] == lista[i-1]+1:
        else:
            return i+1
        i+=1
    return len(lista)+1