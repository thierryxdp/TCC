def busca(setor,matriz):
    nova_lista = []
    for x in matriz:
        if setor in x:
            x.remove(setor)
        return nova_lista
    else: 
            return []