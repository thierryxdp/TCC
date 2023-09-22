def busca(setor,matriz):
    ''''''
    a=0
    for linha in matriz:
        if setor in matriz:
            a=a+linha
            return matriz