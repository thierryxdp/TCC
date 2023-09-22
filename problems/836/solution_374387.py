def busca (setor,matriz):
    '''c'''
    resp=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in j:
                resp+=j
    return resp