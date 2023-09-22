def melhor_volta(m:list)->tuple:
    acumulador=[0,9999999,0]
    for i in range(6):
        for j in range(10):
            if m[i][j]<acumulador[1]:
                acumulador[1]=m[i][j]
                acumulador[0]=i+1
                acumulador[2]=j+1
    return tuple(acumulador)