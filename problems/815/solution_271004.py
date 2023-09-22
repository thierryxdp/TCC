def insere(lista_numero,n):
    ''' Função que dada uma lista ordenada de números inteiros
    (lista_numero) e um número inteiro (n), retorna uma lista
    com n inserida em lista_numero de forma que ela continue
    ordenada.
    Entrada: list,int
    Retorno: list '''
    
    lista_numero[0:0] = [n]
    list.sort(lista_numero)

    return lista_numero