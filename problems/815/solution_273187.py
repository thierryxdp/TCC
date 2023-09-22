def insere(lista_numero,n):
    '''
    Função que dada uma lista ordenada(crescente) de números
    inteiros e um número inteiro n, inclua n na posição correta,
    ou seja, de tal maneira que a lista continue ordenada
    list, int -> list
    '''
    lista_numero[0:0]=n
    inserir=lista_numero.sort()
    
    return inserir