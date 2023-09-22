def busca(matriz,nome):
    x=''
    for a in matriz:
        for b in a:
            if nome == b:
                return matriz[a]
            else:
                return []