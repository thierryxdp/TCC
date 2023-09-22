def busca(matriz,s):
    '''função em que dada uma matriz contendo os dados dos funcionários de uma
    empresa e um setor (s), retorne o dado de todos os funcionários daquele
    setor;
    list,str -> list'''
    f=[]
    for i in range(len(matriz)):
        if matriz[i][2]==s:
            list.append(f,matriz[i])
    return f