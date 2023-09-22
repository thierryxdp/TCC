def busca(s,matriz):
    '''função em que dado um setor e uma matriz contendo os dados dos
    funcionários de uma empresa, retorne o dado de todos os funcionários daquele
    setor;
    str,list -> list'''
    f=[]
    for i in range(len(matriz)):
        if matriz[i][2]==s:
            list.append(f,matriz[i])
    return f