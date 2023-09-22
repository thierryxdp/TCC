def filtra_pares ([p,s,t,q]):
    '''função que recebe uma tupla com 4 entradas (prim,seg,terc,quart) e retorna uma nova tupla com elementos pares da de entrada; tupla->tupla'''
    if (p%2)+(s%2)+(t%2)+(q%2)==0:
        return ([p,s,t,q])