def insere(lista_numero, n):
    """ Função que recebe como parâmetro de entrada uma lista
    ordenada (crescente) e um número inteiro n, faz com n seja
    posto na posição correta e retorna uma lista com os valores
    estabelecidos na entrada só que de maneira ordenada.
    Entrada: list, int
    Saída: list
    """
    
   
    lista_1 = [n]
    lista_2 = list.sort(lista_numero)
    lista_3 = lista_2 + lista_1
    lista_4 = list.sort(lista_4)
    
    return lista_3