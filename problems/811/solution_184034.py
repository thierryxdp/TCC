def colchao (medidas, H, L):
    """funçao que recebe as medidas (A<B<C) com as dimensoes em centimetros de um colchao, a  altura H e largura L de uma porta e retorna verdadeiro de o colchao passa e falso se não;
entrada: list [float, float, float], int, int;
saida: bool."""

    A = medidas [0]
    B = medidas [1]
    C = medidas [2]
    
    maior = max (L, H)
    menor = min (L, H)

    if (A >=  maior) or (B >= maior):
        return False

    elif (B >= maior) or (C >= maior):
        return False

    elif (A >= maior) or (C >= maior):
        return False
    #[22, 188, 216], 193, 99

    else:
        return True