def filtraMultiplos(n):
    '''retorna uma lista com os multiplos de n presentes na lista dada'''
    return list(filter(lambda numero: numero%n == 0, range(n)))