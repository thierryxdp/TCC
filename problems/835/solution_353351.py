def melhor_volta(m):
    ''' funcao que  recebe como entrada uma matriz 6 × 10 com os tempos em segundos dos corredores
em cada volta da corrida e retornar uma tupla informando: De quem foi a melhor volta da prova,
com qual tempo e em que volta. list-> tuple'''
    tupla = ()
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    
    b=[]
    c=[]
    for i in range(qtd_linhas):
        b.append((i+1,min(m[i]),m[i].index(min(m[i]))+1))
        c.append(min(m[i]))
    e=c.index(min(c))
    return b[e]