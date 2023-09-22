def colchao(medidas,H,L):
    """Função que recebe as medidas A,B,C de um colchão em forma de paralelepípedo reto retângulo e as dimensões de uma porta e calcula se esse colchão passa ou não pela porta, retornandno True se passar e False se não.
    list,int,int -> bool
    Explicação: como o colchão pode ser rotacionado e virado, basta que uma das dimensões (B ou C) passe pela altura ou largura da porta para que ele caiba. Assim, basta calcularmos as possibilidades, de acordo com os valores possíveis para B,C,H,L."""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    A<B<C
    if H>L:
        if B<=H or C<=H:
            return True
        else:
            return False
    if L>H:
        if B<=L or C<=L:
            return True
        else:
            return False
    if H==L:
        if B<=H or C<=H:
            return True
        else:
            return False