def busca(string,matriz):
    x = []
    for y in matriz:
        for string in y:
            x = x + [y]
    return x