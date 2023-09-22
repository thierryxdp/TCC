def busca(matriz,l):
    """Cálculo de uma função que recebe como entrada uma matriz e faz uma busca
    por setor e retorna os dados de todos os funcionários daquele setor.
    
       Parameters:
       matriz: matriz que servirá de busca
       
       
       Returns:
       Retorna os dados de todos os funcionários do setor procurado, dado que:
       list,str -> list
    """
    l1=[]
    s=0
    p=''
    for s in range(len(matriz)):
        if str.find(l,p) in str.find(matriz,s):
            list.append(l1,matriz)
            s=s+1
    return l1