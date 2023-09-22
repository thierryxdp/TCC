def maiores(lista_numero:list[int],n:int)->list[int]:
    '''Retorna uma lista com todos os numeros
    maiores que n'''
    lista_numero.append(n)
    lista_numero.sort()
    lista_numero[lista_numero.index(n)+1:]
    return lista_numero