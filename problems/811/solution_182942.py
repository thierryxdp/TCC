# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef colchao(medidas, H, L):
    if (
        medidas[0] <= H
        and medidas[1] <= L
        or medidas[0] <= H
        and medidas[2] <= L
        or medidas[1] <= H
        and medidas[2] <= L
        or medidas[2] <= H
        and medidas[1] <= L
        or medidas[0] <= L
        and medidas[1] <= H
        or medidas[0] <= L
        and medidas[2] <= H
    ):
        return True
    else:
        return False