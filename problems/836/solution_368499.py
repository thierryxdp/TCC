def busca(matriz,l):
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
    matriz = [('AdalbertoFerreira','566','Contabilidade','(21)84564-5248'),('JulianaVasconcelos','465','RH','(21)3555-4552'),('FlaviaAmorim','565','Contabilidade','(21)2134-4845')]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if l in matriz:
                k.append(matriz[i][j],l)
            s=s+1
    return matriz[k]