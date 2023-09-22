def filtra_pares(tupla):
    '''funcao que, dada uma tupla de 4 inteiros, retorna outra tupla apenas com os inteiros
    pares; tuple->tuple'''
    a=int(tupla[0])%2
    b=int(tupla[1])%2
    c=int(tupla[2])%2
    d=int(tupla[3])%2
    tupla=(a,b,c,d)
    if a==0 and b==c==d==1:
        return tupla[0]
    elif a==b==0 and c==d==1:
        return (tupla[0]) + (tupla[1])
    elif a==b==c==0 and d==1:
        return (tupla[0]) + (tupla[1]) + (tupla[2])
    else:
        return (tupla[0]) + (tupla[1]) + (tupla[2]) + (tupla[3])