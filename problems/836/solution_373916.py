def busca(s,M):
    '''Função que da uma matriz M onde cada linha é sobre um
funcionário e cada coluna contem informações dessa pessoa, 
ela retorna, dada uma área s da empresa, as informações das
pessoas que trabalham nessa área;
	str,list -> list'''
    p=[]
    pt=[]
    for i in range(len(M)):
        if s in M[i][2]:
            list.append(p,M[i][0])
            list.append(p,M[i][1])
            list.append(p,M[i][3])
        pt=pt+p
    return pt