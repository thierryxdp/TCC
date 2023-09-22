def insere(lista_numero, n):
    '''
    dada uma lista de números inteiros em ordem
    crescente e um número inteiro, o número inteiro
    é inserido na lista na posição correta
    
    list, int -> list
    '''
    
    lista_numero.insert(0, n)
    lista_numero.sort()
    return lista_numero