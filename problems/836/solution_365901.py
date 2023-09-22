def busca(setor,a):
    """ Retorna a lista com os funcionários do setor em questão; list,string -> list """
    lista=[]
    for i in range(len(a)):
        if setor in a[i][2]:
            del a[i][2];
            list.append(lista,a[i])
    return lista