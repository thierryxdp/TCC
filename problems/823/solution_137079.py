def faltante(lista:list)->int:
    lista=lista.sort()
    i=0
    while i<len(lista):
        if i not in lista:
            saida = i
        i+=1
    return saida