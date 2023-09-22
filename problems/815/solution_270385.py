def insere(lista_numero,n):
    """
    Função que dada uma lista de numeros inteiros e 
    um número inteiro n, inclua n na posição correta, ou seja,
    de tal maneira que a lista continue ordenada.
    Parametro de Entrada: list, int
    Valor de Saida: list
    """
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero