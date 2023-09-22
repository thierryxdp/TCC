def insere (lista_numero: list[int], n: int) -> list[int]:
    '''doc'''
    lista_retorno = lista_numero.copy()
    lista_retorno.sort()
    lista_retorno.append(n)
    lista_retorno.sort()
    
    return lista_retorno