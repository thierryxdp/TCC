def busca(setor,m):
    '''dada uma matriz, busca os dados de todos os funcionarios por setor
    list -> list'''
    
    matriz=[]
    
    for  i in range(len(m)):
        if setor in m[i]:
            matriz.append(m[i][:2]+[m[i][3]])
            
    return matriz