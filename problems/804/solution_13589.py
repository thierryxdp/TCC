def filtra_pares(tupla_inicial):
    '''funcao que, dada uma tupla de 4 inteiros, retorna outra tupla apenas com os inteiros
    pares; tuple->tuple'''
    tupla_inicial=(a,b,c,d)
    tupla=(int(a),int(b),int(c),int(d))
    if tupla[0]%2 == tupla[1]%2 == tupla[2]%2 == tupla[3]%2 == 0:
        return (tupla[0], tupla[1], tupla[2], tupla[3])