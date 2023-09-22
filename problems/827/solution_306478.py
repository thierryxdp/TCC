def qtd_divisores(n):
    '''retorna uma lista com os multiplos de n presentes na lista dada'''
    return list(filter(lambda numero: n%numero == 0, range(n)))