def primo (numero):
    """Função que dada um numero inteiro positivo diz se ele é primo;
    int -> bool"""
    quantidade = 0
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            quantidade += 1
    if quantidade>2:
        return False
    else:
        return True