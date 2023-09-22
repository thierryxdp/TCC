def busca(palavra,matriz):
    """Retorna os dados de todos os funcionarios daquele setor.list-->list"""
    setor=[]
    for i in matriz:
        if matriz[i][2]==palavra:
            setor=setor+[matriz[i][0]+matriz[i][1]+matriz[i][3]]
        else:
            setor=setor
    return setor