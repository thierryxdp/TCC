#Start your python function here
def filtra_pares(tupla):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original e na mesma ordem que eles apareceram. tupla->tupla'''
    if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return tupla
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0:
        return (tupla[0],tupla[1],tupla[2])
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[3]%2==0:
        return (tupla[0],tupla[1],tupla[3])
    elif tupla[0]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (tupla[0],tupla[2],tupla[3])
    elif tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (tupla[1],tupla[2],tupla[3])
    elif tupla[0]%2==0 and tupla[1]%2==0:
        return(tupla[0],tupla[1])
    elif tupla[0]%2==0 and tupla[2]%2==0:
        return(tupla[0],tupla[2])
    elif tupla[0]%2==0 and tupla[3]%2==0:
        return(tupla[0],tupla[3])
    elif tupla[2]%2==0 and tupla[1]%2==0:
        return(tupla[1],tupla[2])
    elif tupla[3]%2==0 and tupla[1]%2==0:
        return(tupla[1],tupla[3])
    elif tupla[2]%2==0 and tupla[3]%2==0:
        return(tupla[2],tupla[3])
    elif tupla[0]%2==0:
        return (tupla[0],)
    elif tupla[1]%2==0:
        return (tupla[1],)
    elif tupla[2]%2==0:
        return (tupla[2],)
    elif tupla[3]%2==0:
        return (tupla[3],)
    else:
        return ()