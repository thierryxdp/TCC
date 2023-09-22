def melhor_volta(mat):
    menores_tempos=[]
    for linhas in mat:
        list.append(menores_tempos,min(linhas))
    menor_t= min(menores_tempos)
    i = list.index(menores_tempos,menor_t)
    volta = list.index(mat[i],menot_t)
    return (i+1 ,menor_t ,volta+1)