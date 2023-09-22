def busca(setor,matriz):
    """retorna os dados de todos os funcionarios daquele setor, caso nenhum registro seja encontrado, retorna uma lista vazia
    str,list(list)->list"""
    a=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(a,matriz[i][0,1,3])
    if len(a)!=0:
        return a
    else:
        return []