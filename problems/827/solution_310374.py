def qtd_divisores(numero):
    qtd = 0
    contador = 0

    while contador <= numero:
        if contador > 0:
            if numero % contador == 0:
                qtd += 1
        contador += 1
    return qtd