def faltante(lista):
    '''Essa funcao recebe uma lista com numeros que nao se repete
       e vai de 1 ate N-1. O programa analisa e ve se ha algum numero
       que quebre a sequencia crescente dos numeros.
       Obs: se os numeros estiverem embaralhados, o programa organiza
       do menor para o maior.

       (list, -> int)'''
    lista.sort()
    qntElementos = len(lista)
    cont = 1
    if lista[0] != 1:
        return 1
    while cont < qntElementos:
        if lista[cont] - lista[cont-1] != 1:
            return lista[cont] - 1
        cont += 1
    return lista[cont-1] + 1 #numero N faltante do final da lista