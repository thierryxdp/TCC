def fatorial(n):
    """Retorna o fatorial do numero n.int-->int"""
    numero=n
    soma=numero
    while numero>0:
        soma=soma*(numero-1)
    numero=numero-1
        return soma