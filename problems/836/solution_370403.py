def busca(setor,matriz):
    """função que recebe como entrada uma matriz que tem quatro entrada referentes a nome,registro,setor e telefone
    e retorna os dados de todos os funciomarios daquele setor"""
    
    lista = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            lista.append(matriz[i])
    for j in range(len(lista)):
        del lista[j][2]
    return lista