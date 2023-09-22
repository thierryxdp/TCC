def busca(nome, x):
    '''Entre com o nome do setor e uma matriz com todos os dados para ser
    retornado uma nova lista com os os dados desse setor
    String, Matriz -> Lista'''
    Nlista=[]
    Nlista2=[]
    n_lin= len(x)
    n_col=len(x[0])

    for i in range(n_lin):
        y=0
        for j in range(n_col):
            y=x[i][j]
            if nome==y:
                list.append(Nlista,x[i][j-2])
                list.append(Nlista,x[i][j-1])
                list.append(Nlista,x[i][j+1])
                
    if len(Nlista)==0:
        return Nlista2
    else:
    	list.append(Nlista2,Nlista)
    	return Nlista2