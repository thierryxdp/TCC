def busca(setor,m):
    '''função que retorna uma lista com os funcionários de um determinado setor; 
    list,list -> list'''
    lista=[]
    for i in range(len(m)):
        if setor in m[i][2]:
            del m[i][2]
            list.append(lista,m[i])
    return lista