def busca(s,M):
    '''Função que da uma matriz M onde cada linha é sobre um
funcionário e cada coluna contem informações dessa pessoa, 
ela retorna, dada uma área s da empresa, as informações das
pessoas que trabalham nessa área;
	str,list -> list'''
    p=[]
    for i in range(len(M)):
        if s in M[i][2]:
            list.remove(M[i],s)
            list.append(p,M[i])
    return p