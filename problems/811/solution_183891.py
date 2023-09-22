# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    ''''Recebe medidas do colchao, altura da porta(H) e largura dela (L). Retorna
    se e possivel passar o colchao pela porta. Inserir lista com medidas A, B, C do colchao (de
    menor para maior) e dois inteiros H e L.
    list, int, int --> boolean'''
    colchao_med = list(zip(medidas))
    A, B, C = medidas[0], medidas[1], medidas[2]
    # em pe:
    if B <= L and C <= H or A <= L and C <= H:
        return True
    # deitado:
    elif A <= H and B <= L or C <= L and A <= H:
        return True
    # de lado:
    elif B <= H and A <= L or C <= L and B <= H:
        return True
    else:
        return False