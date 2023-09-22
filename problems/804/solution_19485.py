def filtra_pares(prim,seg,terc,quart):
    '''função que recebe uma tupla com 4 entradas (prim,seg,terc,quart) e retorna uma nova tupla com elementos pares da de entrada; tupla->tupla'''
    if (prim%2,seg%2,terc%2,quart%2)==0:
        return (prim,seg,terc,quart)
    else:
        if (prim%2==0 and seg%2,terc%2,quart%2)!=0:
            return prim
        else:
            if (seg%2==0 and prim%2,terc%2,quart%2!)=0:
                return seg