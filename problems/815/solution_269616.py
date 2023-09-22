def insere(lista_numero,n):
    ''' Dada uma lista ordenada crescente de números 
    inteiros e um numero inteiro (n), inclui (n) na posicao
    correta, de tal maneiraa que a lisa continue ordenada.
    list, int -> list'''
    
    l=lista_numero
    
    list.append(l,n)
    list.sort(l)
    return l