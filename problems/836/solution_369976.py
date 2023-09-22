def busca(setor,m):
    """essa funcao recebe uma matriz e faz uma busca por setor e retorna os dados de todos os funcionarios daquele setor; str, list-> list""" 
    matriz=[]
    for  i in range(len(m)):
        if setor in m[i]:
            matriz.append(m[i][:2]+[m[i][3]])
    return matriz