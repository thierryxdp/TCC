def busca(nome,m):
    '''retorna os dados de todos os funcionários do setor;
    str,mat->mat'''
    dados=[]
    dados2=[]
    posicaoi=[]
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==nome:
                posicaoi+=[i,]
    
    for j in range(len(m[i])):
        dados+=[m[posicaoi[0][j],]
        dados2+=[m[posicaoi[1][j],]
            
                       
    return dados+dados2