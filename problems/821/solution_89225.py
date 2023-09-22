def fatorial(numero):
    """Dada um número como parâmetro, a função vai calcular 
    o fatorial deste número.
   	int --> int"""
    contaFinal = 1
    while numero > 1:
        if numero > 1:
            contaFinal = contaFinal * numero
        numero = numero - 1
    return contaFinal