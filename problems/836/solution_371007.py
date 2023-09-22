def busca(setor,m):
   matriz = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if setor.upper() in m[i][j].upper():
                matriz.append(contatos[i])
    return matriz