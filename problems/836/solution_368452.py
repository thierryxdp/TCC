busca(matriz,l):
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
    for i in matriz:
        if len(indices)==0:
            indices.append(s.find(i)+1)
        else:
            indices.append(s.find(i,indices[-1])+1)