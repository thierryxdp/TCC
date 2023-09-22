def busca(setor,matriz):
    nova_lista = []
    while len(matriz) != 0:
        for x in matriz:
            if setor in x:
                x.remove(setor)
                return x
            else: 
                return []