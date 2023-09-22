def busca(s,m):
    """ """
    contato=[]
    for i in range(len(m)):
        if s==(m[i][2]):
            contato.append(m[i][:2]+[m[i][-1]])
    return contato