def busca(setor,m):
    '''retorna uma lista com as informações de todos os 
    individuos que estão em dado setor;
    string, matriz -> lista'''
    lista = []
    for i in m:
        for j in i:
            if setor in j:
                list.append(lista, [i[0], i[1], i[3]])
    return lista