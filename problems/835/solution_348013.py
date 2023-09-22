def melhor_volta(lista):
    soma = 0
    for x in lista:
        for y in x-1:
            menor_volta = min(x[y])
            posicao = index(x) + 1
            volta = x[y]+ 1
    return (menor_volta, posicao, volta)