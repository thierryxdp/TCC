def busca(string, matriz):
    ret = []
    for i in matriz:
        if string == i[2]:
            ret.append([i[0], i[1], i[3]])
    return(ret)