def filtra_pares(tupla):
    if tupla[0]%2==0:
        n1=tupla[0]
    else:
        n1=''
    if tupla[1]%2==0:
        n2=tupla[1]
    else:
        n2=''
    if tupla[2]%2==0:
        n3=tupla[2]
    else:
        n3=''
    if tupla[3]%2==0:
        n4=tupla[3]
    final=(n1,n2,n3,n4)
    return final