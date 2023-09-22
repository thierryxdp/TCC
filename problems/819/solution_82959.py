def filtraMultiplos(lista_de_numeros,n):
    '''Função que retorna uma lista com os elementos da lista original que são divisíveis por número, dado a lista de número e o número n; list, int->list'''
    indice=0
    multiplos=[]
    while indice<len(lista_de_numeros):
        if lista_de_numeros[indice]%n==0:
            multiplos= multiplos+[lista_de_numeros[indice]]
        indice= indice+1
    return multiplos