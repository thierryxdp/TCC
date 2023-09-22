def busca(nome,m):
    '''retorna os dados de todos os funcionários do setor;
    str,mat->mat'''
    dados=[]
    
    for i in range(len(m)):
        if m[i][2]==nome:
            dados+=[m[i],]
            else:
                return []
    return dados