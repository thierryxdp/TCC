def colchao (medidas, H, L):
    """funçao que recebe as medidas (A<B<C) com as dimensoes em centimetros de um colchao, a  altura H e largura L de uma porta e retorna verdadeiro de o colchao passa e falso se não;
entrada: list [float, float, float], int, int;
saida: bool."""

    A = medidas [0]
    B = medidas [1]
    C = medidas [2]

    if A and B >= L and H:
        return False

    elif B and C >= L and H:
        return False

    elif C and A >= L and H:
        return False

    else:
        return True