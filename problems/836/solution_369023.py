def busca(nome, x):
    '''Entre com o nome do setor e uma matriz com todos os dados para ser
    retornado uma nova lista com os os dados desse setor
    String, Matriz -> Lista'''
    Nlista=[]
    Nlista2=[]
    n_lin= len(x)
    n_col=len(x[0])

    for i in range(n_lin):
        for j in range(n_col):
            if j==3:
            	break
            if nome==x[i][j]:
                list.append(Nlista,x[i][j-2])
                list.append(Nlista,x[i][j-1])
                list.append(Nlista,x[i][j+1])
                
    if len(Nlista)==0:
        return Nlista2
    else:
    	list.append(Nlista2,Nlista)
    	return Nlista2