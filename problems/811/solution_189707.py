# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef colchao(medidas, H, L):
    """Dado três dimensões de um colchão em centímetro, verifica se esse colchão passa pela porta de altura H e largura L.
    list, int, int -> bool"""
    [A, B, C] = medidas
    if A and B > H and L:
        return False

    else:
        return True


return (colchao([25, 200, 220], 200, 100))