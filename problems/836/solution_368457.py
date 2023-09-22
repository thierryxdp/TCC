def busca(matriz,l):
    """Cálculo de uma função que recebe como entrada uma matriz e faz uma busca
    por setor e retorna os dados de todos os funcionários daquele setor.
    
       Parameters:
       matriz: matriz que servirá de busca
       
       
       Returns:
       Retorna os dados de todos os funcionários do setor procurado, dado que:
       list,str -> list
       """
    baseatual= -1
    indices=[]
    for l in matriz:
        if len(indices)==0:
            indices.append(str.find(matriz,l)+1)
        else:
            indices.append(str.find(l,indices[-1])+1)