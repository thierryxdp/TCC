def colchao(medidas: list, H: int, L: int) -> bool:
    """Recebe as medidas do colchão, a altura da porta e a largura da porta
       e retorna se o colchão passa ou não pela porta

       Parameters:
       medidas: Lista composta por 3 números inteiros na ordem crescente,
       no qual representam as dimensões A (altura), B (largura) e C
       (comprimento), tudo em centímetros
       H: Altura da porta em centímetros
       L: Largura da porta em centímetros

       Return:
       Dados os parâmetros "medidas", "H" e "L", determina se o colchão, que é
       um parelelepípedo reto retângulo, passa ou não pela porta, retornando
       "True" caso passe e "False" caso não passe

       Examples:
       colchao([25, 120, 220], 200, 100) == True
       colchao([25, 205, 220], 200, 100) == False
       colchao([25, 200, 220], 200, 100) == True
    """

    B = medidas[0]
    A = medidas[1]

    return ((A <= H) and (B <= L))