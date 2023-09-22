def busca(s,m):
    lista_retorno=[]
    for i in m:
        if i[2]==s:
        lista_retorno.append(i[0:2]+i[3])
    return lista_retorno