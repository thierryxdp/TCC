def busca(nome,m):
    '''retorna os dados de todos os funcionários do setor;
    str,mat->mat'''
    dados=[]
    dados2=[]
    posicaoi=[]
    i=0
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==nome:
                posicaoi+=[i,]
    while i=posicaoi[0] or i=posicao[1]:
        for j in range(len(m[i])):
            dados+=[m[i][j],]
            dados2+=[m[i][j],]
        i=i+1    
                       
    return dados+dados2