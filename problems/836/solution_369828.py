def busca(st,mt):
    '''Função que retorna os dados de todos os funcionários
    daquele setor dado na entrada.
    st=str,mt=list->list'''
    p=0
    tt=[]
    for w in range(len(mt)):
        if st in mt[p]:
            del mt[p][2]
            tt=tt+[mt[x]
    	p=p+1
    return tt