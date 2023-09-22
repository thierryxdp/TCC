def busca(string, matriz):
    '''funcao que dada uma entrada uma matriz que dada a funcao e setor retorne a mesma
    str, int-> str, int'''
    ret = []
    for i in matriz:
        if string == i[2]:
            ret.append([i[0], i[1], i[3]])
    return(ret)