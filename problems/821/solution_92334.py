def fatorial(n):
    """Função que da o resultado do fatorial de um numero;
    int->int"""
    fator=1
    contador=1
    while contador<=n:
        fator=fator*contador
        contador+=1
    return fator