def busca(l,matriz):
    """Cálculo de uma função que recebe como entrada uma matriz e faz uma busca
    por setor e retorna os dados de todos os funcionários daquele setor.
    
       Parameters:
       matriz: matriz que servirá de busca
       
       
       Returns:
       Retorna os dados de todos os funcionários do setor procurado, dado que:
       list,str -> list
    """
    k=[]
    s=0
    for i in matriz:
        if l == i[2]:
            del(i[2])
            list.append(k,i)
            s=s+1
    return k