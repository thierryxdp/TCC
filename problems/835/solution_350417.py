def melhor_volta(matriz):
    x = []
    z = 0
    while z < len(matriz):
        for y in matriz:
            for k in matriz[z]:
                x = x + [k]
        z = z + 1
    f = min(x)
    d = 0
    while d < len(matriz):
        for y in matriz:
            for k in matriz[z]:
                if f == k :
                    return (d+1, f, list.find(matriz[d],f)+1)
        d = d + 1