def insere(lista_numero: list, n: int) -> list:
    '''
    Retorna lista com o número inteiro dado na posição correta dada uma lista com números em ordem crescrente
    '''
    lista_numero.insert(n, 1)
    return lista_numero