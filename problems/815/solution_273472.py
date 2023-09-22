def insere(lista_numero: list, n: int) -> list:
    '''
    Retorna lista com o número inteiro dado na posição correta dada uma lista com números em ordem crescrente
    '''
    lista_numero.insert(1, n)
    return lista_numero