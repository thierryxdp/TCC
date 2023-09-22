def filtra_pares(tupla):
    '''funcao que, dada uma tupla de 4 inteiros, retorna outra tupla apenas com os inteiros
    pares; tuple->tuple'''
    a=int(tupla[0])%2
    b=int(tupla[1])%2
    c=int(tupla[2])%2
    d=int(tupla[3])%2
    tupla=((a),(b),(c),(d))
    if a==0 and b==c==d==1:
        return (a)
    elif b!=0:
        return (a) + (b)
    elif c!=0:
        return (a) + (b) + (c)
    else:
        return (a) + (b) + (c) + (d)