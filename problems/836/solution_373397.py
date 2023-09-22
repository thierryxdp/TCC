def busca(setor:str,matriz:list)->list:
    lista=[]
    for i in matriz:
        if setor in i[2]:
            i.remove(setor)
            lista+=[i]
    return lista