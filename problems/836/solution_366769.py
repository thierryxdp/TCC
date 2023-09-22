def busca(setor,M):
    """coment"""
    lista=[]
    linhas=range(len(M))
    for i in linhas:
        if M[i][2]== setor:
            list.append(lista,[M[i][0],M[i][1],M[i][3]])
    return lista