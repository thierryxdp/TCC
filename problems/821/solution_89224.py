def fatorial(numero):
    contaFinal = 1
    while numero > 1:
        if numero > 1:
            contaFinal = contaFinal * numero
        numero = numero - 1
    return contaFinal