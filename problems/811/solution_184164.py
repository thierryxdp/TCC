def colchao (medidas, H, L):
    """funçao que recebe as medidas onde A<B<C com as dimensoes em centimetros de um colchao a  altura H e largura L de uma porta e retorna verdadeiro se o colchao passa pela porta e falso se não;
entrada: list [int,int,int], int, int;
saida: bool."""

    A = medidas [0]
    B = medidas [1]
    C = medidas [2]
    
    maior = max (L, H)
    menor = min (L, H)

    if (B> maior):
        return False
    
    elif (B<= maior) and (A> menor):
        return False
    
    else:
        return True