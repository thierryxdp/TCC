def primo(numero):
    """Função que, dado um número inteiro positivo, retorne 'True' se ele for primo e 'False' se não for
    entrada: int
    saída: bool"""
    divisor=2
    while divisor<numero:
        if numero%divisor==0:
            afirmativa=False
        else:
            afirmativa=True
            divisor=divisor+1
    return afirmativa