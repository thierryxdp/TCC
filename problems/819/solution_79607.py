def filtraMultiplos(lista,n):
    '''funcao que recebe como entrada uma lista de numeros e um numero n, e retorna, em uma nova lista, quais numeros da lista de entra sao multiplos de n
    list, float -> list'''
    lista_multiplos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista_multiplos=lista_multiplos+lista[i]
        i=i+1
    return lista_multiplos