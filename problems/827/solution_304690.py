def soma_fatorial():
    """Função que calcula o fatorial dos números inteiros de 1 a 10. Sem entradas."""
    fat = contador = 1
    soma = 0
    for x in range(0, 10):
        for x in range(contador, contador+1):
            fat *= x
        contador += 1
        soma += fat
    return soma