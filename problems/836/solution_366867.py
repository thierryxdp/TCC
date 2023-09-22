def busca(setor,x):
    """Função que retorna uma lista com os funcionarios do setor dado
    list--> list"""
    lista=[]
    for i in range(len(x)):
        if setor in x[i][2]:
            del x[i][2];
            list.append(lista,x[i])
    return lista