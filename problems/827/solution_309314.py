def qtd_divisores(numero):
    contador = 0
    for i in range(0, numero):
        if numero%i == 0:
            contador = contador + 1
            
    return contador