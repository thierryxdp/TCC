def busca(x,m):
    """funcao que dada o setor e a matriz retorne os dados dos funcionários.
    str,list-->list."""
    lista=[]
    for i in range(len(m)):
        if x in m[i]:
            lista.append([m[i][0],m[i][1],m[i][3]])
    return lista