def filtra_pares(tupla):
    """"""
    if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return tupla
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2!=0:
        return '('+str(tupla[3])+')'
    elif tupla[0]%2!=0 and tupla[1]%2==0 and tupla[2]%2!=0 and tupla[3]%2==0:
        return '('+str(tupla[1:])+')'
    elif tupla[0]%2==0 and tupla[1]%2!=0 and tupla[2]%2==0 and tupla[3]%2==0:
        return '('+str(tupla[0])+','+str(tupla[3:])+')'
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2!=0 and tupla[3]%2==0:
        return '('+str(tupla[:2])+','+str(tupla[3])+')'
    elif tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2!=0 and tupla[3]%2!=0:
        return '('+str(tupla[:2])+')'
    elif tupla[0]%2!=0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2!=0:
        return '('+str(tupla[1:3])+')'
    elif tupla[0]%2!=0 and tupla[1]%2!=0 and tupla[2]%2==0 and tupla[3]%2==0:
        return '('+str(tupla[2:])+')'
    elif tupla[0]%2==0 and tupla[1]%2!=0 and tupla[2]%2!=0 and tupla[3]%2==0:
        return '('+str(tupla[0])+','+str(tupla[3])+')'
    elif tupla[0]%2==0 and tupla[1]%2!=0 and tupla[2]%2!=0 and tupla[3]%2!=0:
        return '('+str(tupla[0])+')'
    elif tupla[0]%2!=0 and tupla[1]%2==0 and tupla[2]%2!=0 and tupla[3]%2!=0:
        return '('+str(tupla[1])+')'
    elif tupla[0]%2!=0 and tupla[1]%2!=0 and tupla[2]%2==0 and tupla[3]%2!=0:
        return '('+str(tupla[2])+')'
    elif tupla[0]%2!=0 and tupla[1]%2!=0 and tupla[2]%2!=0 and tupla[3]%2==0:
        return '('+str(tupla[3])+')'