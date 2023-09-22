def maiores(lista_numero, n):
    '''Funcao que recebe uma lista com numeros
    inteiro e um numero inteiro, e retorna uma 
    nova lista com os inteiros maiores que n.
    Dados de entrada: list, int
    Valor de saida: list
    '''  
    lista_ordenada = insere(lista_numero, n)
    posicao_de_n = list.index(lista_ordenada, n)
    lista_maiores_que_n = list(range(posicao_de_n +1, lista_ordenada[-1]+1))
    return lista_maiores_que_n