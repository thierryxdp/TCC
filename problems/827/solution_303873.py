def qtd_divisores(n):
    """ Função que conta quantos divisores um número tem.
    int, int->int """
    checar = [False]*100000
    fator = fator primo(n)
    soma dos divisores = 1
    for x in fator:
        if checar[x]:
            continue
        else:
            count = fator.count(x)
            tmp = ( x**(count+1)-1)//(x-1)
            soma dos divisores *= tmp
            checar[x] = True
    return soma dos divisores