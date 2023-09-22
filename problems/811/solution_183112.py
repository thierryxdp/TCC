# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H, L):
    """
    Função que dada as medidas de um colchão, a altura e largura de uma porta, retorna true se o colchão passar por essa porta e false, se não passar
    list, int, int-> bool
    
    Parameters:
    medidas: Parâmetro do tipo lista que contém 3 números inteiros que representam o tamanho do colchão
    H: Parâmetro do tipo int que representa a altura da porta
    L: Parâmetro do tipo int qu representa a largura da porta
    """

    A,B,C = medidas

    if (H<L):
        troca = H
        H = L
        L = troca

    x= min(A, min(B,C))
    y= min(max(A,B), min(max(A,C), max(B,C)))

    if(x<=L and y<=H):
        return True
    else:
        return False