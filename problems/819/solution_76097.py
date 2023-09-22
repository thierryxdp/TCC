def filtraMultiplos(lista,n):
    '''Escreva uma lista de numeros entre []. Apos isso, digite um
	numero. A funcao retorna os elemetos da lista que forem
    divisiveis pelo numero, ou seja, seus multiplos.
    list, float -> list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n==0:
            multiplos=multiplos+[lista[i]]
        i=i+1
    return multiplos