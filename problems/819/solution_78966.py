def filtraMultiplos(lista,n):
    ''' Função que dados uma lista de números inteiros (lista) e um 
    número (n), retorna uma lista contendo todos os elementos  de 
    lista que forem divisíveis por n.
    Entrada: list, int
    Retorno: list '''
    
    divisiveis = []
    indice = 0
    while indice < len(lista):
        if lista[indice] % n == 0:
            list.append(divisiveis,lista[indice])
        indice += 1
        
    return divisiveis