def insere(lista_numero,n):
    ''' Função que dada uma lista ordenada de números inteiros
    (lista_numero) e um número inteiro (n), retorna uma lista
    com n inserida em lista_numero de forma que ela continue
    ordenada.
    Entrada: list
    Retorno: list '''
    
    insercao = [n] + lista_numero
    lista_ordenada = list.sort(insercao)
    return lista_ordenada