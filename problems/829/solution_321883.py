def equacaoE():
    """..."""
    soma = 0
    i=1
    while i<=10000:
        soma = soma + (1.0/i)*((-1)**(i+1))
        i=i+1
    return soma