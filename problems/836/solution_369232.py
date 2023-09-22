def busca(setor,matriz):
    lista_nova = []
    contador = 0
    for i in matriz:
        if setor == i[2]:
            del(i[2])
            lista_nova.append(i)
    return lista_nova