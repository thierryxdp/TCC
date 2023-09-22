def colchao(medidas,H,L):
    """função que recebe como entrada uma lista com as dimensoes
    do colchao em centimetros,ordenadas da menor para a maior, e dois
    inteiros H e L, correpondentes respectivamentes a altura e a largura
    das portas em centimetros.A função retorna true se o colchão passa
    pela porta e false caso ele não passe.
    lista(int,int,int)int,int-> bool
    """

    if medidas[2]<=H and medidas[2]<=L:
        return True
    elif medidas[2]<=H and medidas[2]>L:
        if medidas [1]<=L: 
            return True
    elif medidas[2]<=H and medidas[2]>L:
        if medidas[0]<=L:
            return True
    elif medidas[2]>H and medidas[2]<=L:
        if medidas[0]<=H:
            return True
    elif medidas[2]>H and medidas[2]<=L:
        if medidas[1]<=H:
            return True
    elif medidas[1]<=H and medidas[1]<=L:
        return True
    elif medidas[1]<=H and medidas[1]>L:
        if medidas[0]<=L:
            return True
    elif medidas[1]>H and medidas[1]<=L:
        if medidas[0]<=H:
            return True
    else:
        return False# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis