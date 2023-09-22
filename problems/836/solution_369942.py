def busca(matriz, setor_matriz):
    ''''''
    lista_matriz=[]
    i = 0
    for i in range(matriz):
        if i[2] == setor_matriz:
            i.remove(setor_matriz)
            lista_matriz.append(i)
            
    return lista_matriz