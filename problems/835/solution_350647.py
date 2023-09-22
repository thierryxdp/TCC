def melhor_volta(matriz):
    x = 0
    minima1 = 1000
    corredor = 0
    volta = 0
    z = 0
    
    while x < len(matriz):
        z = 0
        for i in matriz[x]:
            z = z + 1
            if minima1 > i:
                minima1 = i
                volta = z
                corredor = x
        x = x + 1
    return (corredor+1, minima1,volta)