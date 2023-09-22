def insere(lista_numero,n):
    '''Função que recebe uma lista e um número inteiro, 
    que entra na lista sem alterar a sua ordenação.
    list, int -> list'''
    
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero