def busca(palavra,matriz):
    """Retorna os dados de todos os funcionarios daquele setor.list-->list"""
    setor=[]
    for i in range(len(matriz)):
        L=matriz[i]
        if L[2]==palavra:
            setor=setor+[str.L[0]+' '+str.L[1]+ ' '+str.L[3]]
        else:
            setor=setor
    return setor