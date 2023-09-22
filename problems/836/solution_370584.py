def busca(setor, matriz):
    lista = []
    for i in matriz:
        if setor in i:
            contato = i
            contato.pop(2)
            lista.append(contato)
    return lista