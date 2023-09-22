def busca(nome, x):
    '''Entre com o nome do setor e uma matriz com todos os dados para ser
    retornado uma nova lista com os os dados desse setor
    String, Matriz -> Lista'''
    Nlista=[]
    n_lin= len(x)
    n_col=len(x[0])

    for i in range(n_lin):
        for j in range(n_col):
            y=x[i][j]
            if nome==y:
                list.append(Nlista,x[i][j])
                list.append(Nlista,x[i][j])
                list.append(Nlista,x[i][j])

    return Nlista