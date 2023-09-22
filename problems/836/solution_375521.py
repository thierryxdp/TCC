def busca(setor,matriz):
    for sublista in matriz:
        if setor in sublista[2]:
            return sublista
        else:
            return []