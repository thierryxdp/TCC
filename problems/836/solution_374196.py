def busca(setor, matriz):
    'descrição'
    for i in matriz:
        for j in i:
            if setor in j:
                return True