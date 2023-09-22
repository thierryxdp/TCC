def busca(s,m):
    """ Dada uma matriz com 4 colunas e linhas variáveis,
    retorna todos os funcionários que trabalham no setor s
    str,list -> list"""
    l = []
    for a in m:
        if s in a[2]:
            a.del(2)
            l.append(a)
    return l