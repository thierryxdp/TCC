def busca(setor,matriz):
    ''' recebe o nome de um setor de uma empresa e uma matriz com as informações de cada funcionario da empresa e retorna uma lista com os dados dos funcionarios daquele setor;str,lista->lista'''
    lista=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for m in range(nlin):
        lista1=[]
        for n in range(ncol):
            if matriz[m][n]==setor:
                lista1.append(matriz[m])
       	lista.append(lista1)
    return lista