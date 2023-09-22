def melhor_volta(m):
    tupla = ()
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    
    b=[]
    c=[]
    for i in range(qtd_linhas):
        b.append((i+1,min(m[i]),m.index(min(m[i]))+1))
        c.append(min(m[i]))
    e=c.index(min(c))
    return b[e]