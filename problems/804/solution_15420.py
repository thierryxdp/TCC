def filtra_pares(tupla):
    '''receber quatro numeros de uma tupla e mostrar apenas os pares
tuple[int, int, int, int] -> tuple '''
    if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return tupla[0],tupla[1],tupla[2],tupla[3]
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0:
        return tupla[0],tupla[1],tupla[2]
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[3]%2==0:
        return tupla[0],tupla[1],tupla[3]
    elif tupla[0]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return tupla[0],tupla[2],tupla[3]
    elif tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return tupla[1],tupla[2],tupla[3]
    elif tupla[0]%2==0 and tupla[1]%2==0:
        return tupla[0],tupla[1]
    elif tupla[0]%2==0 and tupla[2]%2==0:
        return tupla[0],tupla[2]
    elif tupla[0]%2==0 and tupla[3]%2==0:
        return tupla[0],tupla[3]
    elif tupla[1]%2==0 and tupla[2]%2==0:
        return tupla[1],tupla[2]
    elif tupla[1]%2==0 and tupla[3]%2==0:
        return tupla[1],tupla[3]
    elif tupla[2]%2==0 and tupla[3]%2==0:
        return tupla[2],tupla[3]
    elif tupla[0]%2==0 and not (tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0):
        return tupla[0],
    elif tupla[1]%2==0 and not (tupla[0]%2==0 and tupla[2]%2==0 and tupla[3]%2==0):
        return tupla[1],
    elif tupla[2]%2==0 and not (tupla[0]%2==0 and tupla[1]%2==0 and tupla[3]%2==0):
        return tupla[2],
    elif tupla[3]%2==0 and not (tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0):
        return tupla[3],
    else:
        return ()#Start your python function here