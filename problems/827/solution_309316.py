def qtd_divisores(numero):
    contador = 1
    for i in range(1, numero):
        if numero%i == 0:
            contador = contador + 1
            
    return contador