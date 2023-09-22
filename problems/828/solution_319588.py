def primo(x): 
    """ Dado um número int positivo, a função verifica se este número
    é primo ou não.
    assinaura: int--> bool
    """
    resultado = [i for i in range(1, x + 1) if x % i == 0]
    if len(resultado) == 2:
        return True
    else:
        return False