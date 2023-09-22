def filtra_pares(tupla):
    '''funcao que dada uma tupla retorna
    apenas os elementos pares; tuple->tuple'''
    if tupla[0]%2==0:
        return (tupla[0])
    elif tupla[0]%2==0 and tupla[1]%2==0:
        return (tupla[0],tupla[1])
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0:
        return (tupla[0], tupla[1], tupla[2])
    else:
        ( )