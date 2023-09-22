# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(compras, produtos):
    total = 0
    for produto in compras:
        total += produtos[produto]
        return round (total,2)