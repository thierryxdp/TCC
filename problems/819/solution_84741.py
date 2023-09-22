def filtraMultiplos(lista_n,n):
    ''' função que recebe uma lista
    e um número e retorna a lista com
    os itens inseridos que forem divisíveis pelo numero'''
    
    x = 0
    contador = 0
    lista = []
    
    while contador <len(lista_n):
        
        posicao = lista_n[x]
        if posicao%n == 0:
            lista.append(posicao)
        contador = contador + 1
        x = x+1

    return lista