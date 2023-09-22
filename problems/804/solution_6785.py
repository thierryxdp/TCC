def filtra_pares (tupla):
    '''retorna os números pares inteiros de uma tupla. tuple(int,int,int,int)->
    tuple'''
    t2=(,)
    if tupla[0]%2==0:
        t2 = t2 + (tupla[0],)
    if tupla[1]%2==0:
        t2 = t2 + (tupla[1],)
    if tupla[2]%2==0:
        t2 = t2 + (tupla[2],)
    if tupla[3]%2==0:
        t2 = t2 + (tupla[3],)
        return t2