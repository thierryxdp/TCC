def colchao(medidas, H, L):
    '''Identifica se o colchão passa ou não pelas portas. Recebe como
    parâmetros uma lista com as dimensões A, B e C do colchão em centímetros
    (sendo A < B < C), a altura "H" da porta em centímetros e a largura "L"
    da porta, também em centímetros.

    list[int, int, int], int, int -> bool'''

    A = medidas[0]
    B = medidas[1]
    C = medidas[2]

    jeito1 = (B <= L) and (C <= H)
    jeito2 = (A <= L) and (C <= H)
    jeito3 = (B <= L) and (A <= H)
    jeito4 = (C <= L) and (B <= H)
    jeito5 = (C <= L) and (A <= H)
    jeito6 = (A <= L) and (B <= H)

    possibilidade = jeito1 or jeito2 or jeito3 or jeito4 or jeito5 or jeito6

    return possibilidade