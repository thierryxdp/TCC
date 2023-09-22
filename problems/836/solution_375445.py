def busca(setor, matriz):
    lista_matriz=[]
    
    for i in matriz:
        if i[2] == setor:
            i.remove(setor)
            lista_matriz.append(i)
            
    return lista_matriz