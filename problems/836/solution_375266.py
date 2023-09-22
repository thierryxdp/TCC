def busca(setor_empresa, matriz):
    lista_matriz=[]
    
    for i in matriz:
        if i[2] == setor_empresa:
            i.remove(setor_empresa)
            lista_matriz.append(i)
            
    return lista_matriz