def faltante(lista:list)->int:
    i=1
    while i<len(lista):
        if i not in lista:
            saida = i
        i+=1
    return i