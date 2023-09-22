def busca(nome,m):
    '''retorna os dados de todos os funcionários do setor;
    str,mat->mat'''
    dados=[]
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==nome:
                dados+=[m[i][1],m[i][2],m[i][3],m[i][4],]        
                       
    return dados