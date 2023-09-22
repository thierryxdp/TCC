def qtd_divisores(numero):
    contador = 0
    limite = numero + 1
    for i in range(0,limite):
        if (numero//i) == 0:
            contador += 1
    return contador