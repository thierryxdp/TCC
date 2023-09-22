def busca(setor,m):
    '''busca na matriz informada os funcionários que 
    trabalham no determinado setor
    str,list(list) -> list(list)'''
    
    res = []
    
    for i in m:
        for j in i:
            if j == setor:
                indice = list.index(j,i)
                del i[indice]
                res += [i,]
                
    return res