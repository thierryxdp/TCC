def busca(busca_setor,m):
    lista=[]
    for linha in range(len(m)):
        if busca_setor == m[linha][2]:
            lista.append([m[linha][0],m[linha][1],m[linha][3]])
    return lista