def qtd_divisores(numero):
    contagem = 0
    for possivel_divisor in range(numero, 0, -1):
        if numero % possivel_divisor == 0:
            contagem += 1
            
    return contagem