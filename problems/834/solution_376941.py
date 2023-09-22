def media_matriz(m):
    nlin = len(m)
    if nlin == 0:
        return 0
    else:   
        ncol = len(m[0])
        if nlin == 0:
            return 0
        else:
            lista = []
            for i in range(nlin):
                for j in range(ncol):
                    list.append(lista,m[i][j])
            x = sum(lista)
            y = len(lista)
            return x/y