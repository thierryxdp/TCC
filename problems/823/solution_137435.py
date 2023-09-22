def somaAleatoria():

    num = 0
    soma = 0
    lista_num = []
    while num != 5:
        soma = soma + num
        num = randint(1,10)
        lista_num.append(num)

    return soma, lista_num