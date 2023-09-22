def filtra_pares(tupla):
    '''funcao que, dada uma tupla de 4 inteiros, retorna outra tupla apenas com os inteiros
    pares; tuple->tuple'''
    a=int(tupla[0])%2
    b=int(tupla[1])%2
    c=int(tupla[2])%2
    d=int(tupla[3])%2
    if a==b==c==d==0:
        return (tupla[0],tupla[1],tupla[2],tupla[3])