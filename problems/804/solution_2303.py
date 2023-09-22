def filtra_pares(tupla):
    '''Função que retorna uma tupla contendo apenas os elementos pares da tupla original de quatro elementos; tuple(int,int,int,int) -> tuple'''
    tuplanova = ()
    testetupla0 = tupla[0]%2
    testetupla1 = tupla[1]%2
    testetupla2 = tupla[2]%2
    testetupla3 = tupla[3]%2
    if testetupla0 == 0:
    tuplanova+ = (tupla[0],)
    if testetupla1 == 0:
    tuplanova+ = (tupla[1],)
    if testetupla2 == 0:
    tuplanova+ = (tupla[2],)
    if testetupla3 == 0:
    tuplanova+ = (tupla[3],)
        return tuplanova