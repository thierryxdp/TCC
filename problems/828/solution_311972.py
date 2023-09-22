def primos(numero):
    """Função dado um numero inteiro positivo retorna se ele é positivo ou não.
    int --> bool"""
    if nummero < 2:
        return False
    else:
        for n in range(2, numero):
            if numero % n == 0:
                return False
            else:
                return True