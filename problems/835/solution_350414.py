def melhor_volta(matriz):
    x = []
    while z < len(matriz):
        for y in matriz:
            for k in matriz[z]:
                x = x + k
        z = z + 1
    f = min(x)
    while z < len(matriz):
        for y in matriz:
            for k in matriz[z]:
                if f == k :
                    return (z+1, f, list.find(matriz[z],f)+1)
        z = z + 1