def colchao (medidas, H, L):
    """funçao que recebe as medidas A,B,C que sao dimensoes de um colchao onde A<B<C, a  altura H e largura L de uma porta e retorna true se o colchao passa por ela e false se não;
entrada: list[int,int,int], int, int;
saida: bool."""

    A = medidas [0]
    B = medidas [1]
    C = medidas [2]

    if B > max(H,L):
        return False
    else:
        if A > min(H,L):
            return False
        else:
            return True