def qtd_divisores(numero):
    divisores = 0
    contador = 1
    if numero >= 0:
        while contador <= numero:
            if numero%contador == 0:
                divisores = divisores + 1
            else:
                divisores = divisores
            contador = contador + 1
        return divisores
    else:
        return 0