def busca(setor,ls):
    nova_lista = []
    for listas in ls:
        if listas[2] == setor:
            del listas[2]
            nova_lista.append(listas)
    return nova_lista