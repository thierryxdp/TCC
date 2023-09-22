def busca(setor:str,matriz:list)->list:
    lista=[]
    for i in matriz:
        matriz.remove(setor)
        if setor in i[2]:
            
            lista+=[i]
    return lista