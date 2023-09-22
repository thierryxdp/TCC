def busca(s,m):
    """ Dada uma matriz com 4 colunas e linhas variáveis,
    retorna todos os funcionários que trabalham no setor s
    str,list -> list"""
    l = []
    for a in m:
        m = []
        if s in a[2]:
            m.append(a[0])
            m.append(a[1])
            m.append(a[3])
        l.append(m)
    return l