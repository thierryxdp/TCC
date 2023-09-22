def buscaSetor(string, matriz):
    ret = []
    for i in matriz:
        if string == i[2]:
            ret.append(i)
    return(ret)