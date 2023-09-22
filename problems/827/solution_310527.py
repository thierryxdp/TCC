def qtd_divisores(numero):
    cont = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1
            return cont