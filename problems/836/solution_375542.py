def busca(setor,matriz):
    nova_lista = []
    for x in matriz:
        if setor in x:
            nova_lista.append(x)
            nova_lista.remove(setor)
        return nova_lista
    else: 
            return []