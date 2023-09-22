def melhor_volta(matriz):
    i=0
    for i in range(1,7):
        if min(matriz[-i])<min(matriz[-i+1]):
            i+=1
    return i