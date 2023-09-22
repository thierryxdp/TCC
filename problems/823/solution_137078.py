def faltante(lista:list)->int:
    lista=lista.sort()
    contador=0
    i=0
    while contador<len(lista):
        if lista[i]!=lista[i]+1:
            saida= lista[i+1]
        i+=1
    return saida