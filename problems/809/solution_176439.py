def intercala(L1, L2):
    'Função que intercala 2 listas e retorna uma terceira lista com os valores das duas primeiras'
    L3 =[ ]
    for i in range(0,len(L1)):
        L3.append(L1[i])
        L3.append(L2[i])
    return L3