# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Retorne verdadeiro se as medidas do colchão passarem pela porta e falso se o colchão for maior que a porta e não passe ;
    list, int, int -> bool"""
    menor_lado_cama = medidas[1]
    menor_lado_cama = medidas[0]
    if H >= L:
        maior_lado_porta = H
        menor_lado_porta = L
    else:
        maior_lado_porta = L
        menor_lado_porta = H
    if menor_lado_cama <= maior_lado_porta:
        if menor_lado_cama <= menor_lado_porta:
            return True
    else:
        return False