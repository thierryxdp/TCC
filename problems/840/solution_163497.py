def bolos(a,b,c):
    '''calcula a quantidade de bolos que pode ser feita dada a quantidade de ingredientes'''
    xicara=a//2
    ovos=b//3
    leite=c//5
    return min(xicara,ovos,leite)