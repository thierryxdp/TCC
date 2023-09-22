def filtra_pares(dados):
    '''retorna os números pares'''
    if (dados[0]%2)==0 and (dados[1]%2)==0 and (dados[2]%2)==0 and (dados[3]%2)==0:
        return dados[0],dados[1],dados[2],dados[3]
    elif dados[0]%2==0 and dados[1]%2==0 and dados[2]%2==0:
        return dados[0],dados[1],dados[2]
    elif dados[0]%2==0 and dados[1]%2==0 and dados[3]%2==0:
        return dados[0],dados[1],dados[3]
    elif dados[0]%2==0 and dados[2]%2==0 and dados[3]%2==0:
        return dados[0],dados[2],dados[3]
    elif dados[1]%2==0 and dados[2]%2==0 and dados[3]%2==0:
        return dados[1],dados[2],dados[3]
    elif dados[0]%2==0 and dados[1]%2==0:
        return dados[0],dados[1]
    elif dados[0]%2==0 and dados[2]%2==0:
        return dados[0],dados[2]
    elif dados[0]%2==0 and dados[3]%2==0:
        return dados[0],dados[3]
    elif dados[1]%2==0 and dados[2]%2==0:
        return dados[1],dados[2]
    elif dados[1]%2==0 and dados[3]%2==0:
        return dados[1],dados[3]
    elif dados[2]%2==0 and dados[3]%2==0:
        return dados[2],dados[3]
    elif dados[0]%2==0:
        return dados[0],
    elif dados[1]%2==0:
        return dados[1],
    elif dados[2]%2==0:
        return dados[2],
    elif dados[3]%2==0:
        return dados[3],
    else:
        return()#Start your python function here