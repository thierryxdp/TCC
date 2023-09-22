def filtra_pares (tupla):
    '''retorna os números pares inteiros de uma tupla. tuple(int,int,int,int)->
    tuple'''
    t2 = tuple()
    if tupla[0]%2==0:
        t2 = t2 + (tupla[0],)
    if tupla[2]%2==0:
        t2 = t2 + (tupla[2],)
    if tupla[4]%2==0:
        t2 = t2 + (tupla[4],)
    if tupla[6]%2==0:
        t2 = t2 + (tupla[6],)
        return t2