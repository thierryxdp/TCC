def filtra_pares(a,b,c,d):
    '''funcao que, dada uma tupla de 4 inteiros, retorna outra tupla apenas com os inteiros
    pares; tuple->tuple'''
    tupla=(a,b,c,d)
    a=int(tupla[0])%2
    b=int(tupla[1])%2
    c=int(tupla[2])%2
    d=int(tupla[3])%2
    if a==0 and b==c==d==1:
        return (a)
    elif b!=0:
        return tupla(a) + tupla(b)
    elif c!=0:
        return tupla(a) + tupla(b) + tupla(c)
    else:
        return tupla(a) + tupla(b) + tupla(c) + tupla(d)