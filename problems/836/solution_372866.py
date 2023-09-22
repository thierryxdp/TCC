def busca(setor,matriz):
    ''''''
    pos=0
    for lista in matriz:
        if setor in lista:
            pos=pos+lista
    return matriz