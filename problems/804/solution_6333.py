def filtra_pares(tupla):
    '''função que recebe uma tupla com quatro elementos inteiros e retorna
    uma tupla nova com apenas números pares na mesma ordem
    tuple->tuple'''
    parA=tupla[0]%2 
    parB= tupla[1]%2 
    parC= tupla[2]%2 
    parD= tupla[3]%2 
    if parA==0 and parB==0 and parC==0 and parD==0:
        return tuple(tupla)
    elif parA==0 and  parB==0 and parC==0 and parD!=0:
        return tuple(tupla[0:3])
    elif parA==0 and parB==0 and parC!=0 and parD==0:
        return tuple(tupla[0:2], tupla[3])
    elif parA==0 and parB!=0 and parC==0 and parD==0:
        return tuple(tupla[0], tupla[2:4])
    elif parA!=0 and parB==0 and parC!=0 and parD==0:
        return tuple(tupla[1:4])
    elif parA==0 and parB==0 and parC!=0 and parD!=0:
        return tuple(tupla[0:2])
    elif parA==0 and parB!=0 and parC==0 and parD!=0:
        return tuple(tupla[0],tupla[:2])
    elif parA==0 and parB!=0 and parC!=0 and parD==0:
        return tuple(tupla[0], tupla[3])
    elif parA!=0 and parB==0 and parC==0 and parD!=0:
        return tuple(tupla[1:3])
    elif parA!=0 and parB==0 and parC!=0 and parD==0:
        return tuple(tupla[1], tupla[3])
    elif parA!=0 and parB!=0 and parC==0 and parD==0:
        return tuple(tupla[2:4])
    elif parA==0:
        return tuple(tupla[0])
    elif parB==0:
        return tuple(tupla[1])
    elif parC==0:
        return tuple(tupla[2])
    elif parD==0:
        return tuple(tupla[3])
    else:
        return 'Não há número par.'