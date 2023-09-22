def busca(setor,matriz):
    nova_lista = []
    for x in matriz:
        if setor in x:
            x.remove(setor)
            return x
        else: 
            return []