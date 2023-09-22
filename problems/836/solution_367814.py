def busca(setor,matriz):
    novamatriz = []
    for i in matriz:
        lista = []
        for j in i:
            if j == setor:
                lista.append(i[0])
                lista.append(i[1])
                lista.append(i[3])
        if lista != []:
            novamatriz.append(lista)
    return novamatriz