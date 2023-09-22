def conta_numero(numero,matriz):
    ''' retorna quantas vezes o numero ocorre na matriz dada
    int, list(list) -> int'''
    i=0
    x=0
    for li in range(len(matriz)):
        for co in range(len(matriz[i])):
            if numero == matriz[li][co]:
                x+=1
        i+=1
    return x