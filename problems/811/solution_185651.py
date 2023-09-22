def colchao(medidas, H, L):
    """Dados uma lista com as dimensões do colchão em centímetros, ordenadas da menor para maior
    e dois inteiros (H e L) que correspodem, respectivamente a altura e a largura da porta em cm.
    A função retorna: True, se o colcão passa pelas portas e False: se o colchão não passa
    list, int, int -> bool"""
    return medidas[1] <= H or medidas[1] <= H