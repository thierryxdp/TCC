def busca(setor,matriz):
    '''
    '''
    lista = []
    a = len(matriz)
    for i in range(a):
        for j in matriz[i]:
            if j == setor:
                lista.append(matriz[i])
    
    c = del lista[2]         
    return  lista