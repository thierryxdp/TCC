def maiores(lista_numero, n):
    '''
    recebe uma lista de inteiros lista_numero e um inteiro n e retorna uma lista
    com os inteiros de lista_nuero maiore que n
    
    list, int -> list
    '''
    lista_n=insere(lista_numero, n)
    list.reverse(lista_n)
    posicao=list.index(lista_n,n)
    lista_maior=lista_n[:posicao]
    list.reverse(lista_maior)
    return lista_maior