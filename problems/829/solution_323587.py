def soma_h(N):
    """
    função que recebe um numero inteiro N e retorna o valor de H(soma da sequência apresentada), que se dá pela
    somente com duas casas decimais.
   int---.float 
    """
    acumulador = 0
    for i in range(1, N + 1):
        H = 1 / i
        acumulador += H

    return round(acumulador, 2)