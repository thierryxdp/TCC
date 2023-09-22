def busca(s,m):
    """
   	Retorna as informacoes relacionadas a busca realizada
    str,list -> list
    """
    r=[]
    m2=m[::]
    for i in range(len(m)):
        if s in m[i][2]:
            m2[i].remove(m[i][2])
            r.append(m2[i])
    return r