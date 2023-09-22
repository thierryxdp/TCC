def filtraMutiplos(lista,n):
    '''Função que dado um numero n e uma lista de numeros, retorna todos os multiplos de n
    list, int -> list'''
    multiplos = []
    indice = 0 
    while indice <len(lista):
        if lista[indice] % n == 0:
            multiplos += (lista[indice],)
        indice = indice + 1
    return multiplos