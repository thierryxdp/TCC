def busca(string,matriz):
    x = []
    for y in matriz:
        if string in y:
            x = x + [y[0],y[1],y[3]]
    return x