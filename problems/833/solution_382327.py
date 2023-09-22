def conta_numero(numero,matriz):
    '''funcao que  dado um numero inteiro e uma matriz de inteiros,retorna quantas vezes o numero aparece na matriz;
    int,int-->int'''
    t = 0
    for l in matriz:
        for n in l:
            if n == numero:
                t +t + 1
                return t