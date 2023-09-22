def busca(nome, x):
    '''Entre com o nome do setor e uma matriz com todos os dados para ser
    retornado uma nova lista com os os dados desse setor
    String, Matriz -> Lista'''
    Nlista=[]
    Nlista2=[]
    n_lin= len(x)
    n_col=len(x[0])

    for i in range(n_lin):
        list.append(Nlista2,Nlista)
        for j in range(n_col):
            y=x[i][j]
            if nome==y:
                list.append(Nlista,x[i][j-2])
                list.append(Nlista,x[i][j-1])
                list.append(Nlista,x[i][j+1])

    return Nlista2