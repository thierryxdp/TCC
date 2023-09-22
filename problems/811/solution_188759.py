def colchao(medidas,H,L):
    '''dada as medidas do colchão e da porta, retorna 'true'
    caso o colchão passe e 'false' caso não passe;
    list,int,int -> bool'''
    if colchao[0][0]<colchao[1] and colchao[0][1]<colchao[2]:
        return 'true'
    elif colchao[0][0]<colchao[2] and colchao[0][1]<colchao[1]:
        return 'true'
    else:
        return 'false'