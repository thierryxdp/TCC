def qtd_divisores(numero):
    ''' função que define a quantidade de divisores de um certo número.
        int ---> int '''
    quantidade_de_divisores = []
    a = numero
    for numero in range(1,a+1):
        if a % numero == 0:
            list.append(quantidade_de_divisores, numero)
            numero -= 1
        else:
            numero -=1
    return len(quantidade_de_divisores)