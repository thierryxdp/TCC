def busca(nome,m):
    '''retorna os dados de todos os funcionários do setor;
    str,mat->mat'''
    dados=[]
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==nome:
                while i==1:
                    for j in range(len(m[i])):
                        dados+=[m[i][j],]
                       
    return [dados]