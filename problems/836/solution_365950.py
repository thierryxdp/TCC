def busca(setor,matriz):
    """A funcao busca em uma matriz, com funcionarios e suas informcoes, o setor, e retorna
todos os funcionarios que ali trabalham.A entrada consite no elemento de busca seguido da 
matriz com os funcionarios.str,list(matriz)->list"""
    matriz1 = []
    for i in range(len(matriz)): 
        for setores in matriz[i]:
            if setor == setores:
                list.append(matriz1,matriz[i])
                del(matriz1[i-1][2])
    return matriz1