def qtd_divisores(n):
    '''retorna uma lista com os multiplos de n presentes na lista dada'''
    lista = list(filter(lambda numero: n%numero == 0, range(1, n)))
    return 0 if len(lista) == 0 else len(lista) + 1