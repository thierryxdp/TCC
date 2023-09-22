def faltante(lista:list)->int:
    i=0
    while i<len(lista):
        if i not in lista:
            saida = i
        i+=1
    return i