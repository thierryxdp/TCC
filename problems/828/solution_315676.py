def primo(numero):
    """Função que, dado um número inteiro positivo, retorne 'True' se ele for primo e 'False' se não for
    entrada: int
    saída: bool"""
    divisor=2
    divisores=0
    while divisor<numero:
        if numero%divisor==0:
            divisores=divisores+1
            divisor=divisor+1
        else:
            divisor=divisor+1
    if divisores>=1:
        return False
    else:
        return True