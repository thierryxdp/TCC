#Start your python function here
def filtra_pares(tupla):
    if tupla[0:]%2==0:
        return tupla[0:]
    elif tupla[0]%2==0and tupla[1]%2==0and tupla[2]%2==0:
        return tupla[0,1,2]
    elif tupla[0]%2==0and tupla[1]%2==0and tupla[3]%2==0:
        return tupla[0,1,3]
    elif tupla[1]%2==0and tupla[2]%2==0and tupla[3]%2==0:
        return tupla[1,2,3]
    elif tupla[0]%2==0and tupla[2]%2==0and tupla[3]%2==0:
        return tupla[0,2,3]
    elif tupla[0]%2==0and tupla[1]%2==0:
        return tupla[0,1]
    elif tupla[1]%2==0and tupla[2]%2==0:
        return tupla[1,2]
    elif tupla[2]%2==0and tupla[3]%2==0:
        return tupla[2,3]
    elif tupla[1]%2==0and tupla[3]%2==0: