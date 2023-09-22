def insere(lista,n):
    '''
    função que recebe um numero e adiciona ele na ordem crescente
    de uma lista
    list, int -> list
    '''
    lista.append(n)
    
    return list.sort(lista)