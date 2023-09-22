def filtraMultiplos(lista,n):
    '''Função que recebe uma lista e um número n e retorna uma nova lista com os valores
multiplos de n
Entrada(lista)
Saída(lista)'''
    pares=[]
    indice=0
    while indice < len(lista):
        if lista[indice] % n == 0:
            pares=pares+[lista[indice],]
        indice=indice+1
    return pares