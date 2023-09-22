def busca(m,setor):
    """Dada uma matriz com informações dos funcionários, retorna todos os funcionários do setor buscado, encontrados dentro da matriz.
    list,str->list"""
    l2=[]
    for i in range(len(m)):
        for j in m[i]:
            if setor==m[i][2]:
                l2=l2+[m[i],]
    return l2