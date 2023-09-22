def busca(setor,matriz):
    for sublista in matriz:
        if setor in sublista[2]:
            sublista.remove(setor)
            return sublista
        else:
            return []