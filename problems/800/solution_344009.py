# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(compras, precos):
    total = 0
    for item in compras:
        total = total + precos[item]
    return round(total, 2)