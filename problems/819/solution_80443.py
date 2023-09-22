def filtraMultiplos(lista,n):
    '''
    	Função que recebe uma lista de
        números e um número n, e retorna
        outra lista contendo os números 
        da lista original que são 
        divisíveis por n
        : param lista: list
        : param n: int
        : return: list
    '''
    lista_multiplos = []
    indice = 0
    
    while indice < len(lista):
        if lista[indice]%n == 0:
            list.append(lista_multiplos,lista[indice])
        indice = indice + 1
        
    return lista_multiplos