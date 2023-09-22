def busca(s,M):
    '''Função que da uma matriz M onde cada linha é sobre um
funcionário e cada coluna contem informações dessa pessoa, 
ela retorna, dada uma área s da empresa, as informações das
pessoas que trabalham nessa área;
	str,list -> list'''
    p=[]
    for i in range(len(M)):
        for j in range(len(M)[i]):
            if str in M[i][j]:
                M1=M[i]
                p=p+del M1[j]
    return p