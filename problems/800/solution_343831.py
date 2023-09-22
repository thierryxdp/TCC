# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(compras, precos):
    valor = 0
    for i in compras:
        if i in precos:
            valor += precos[i]
    return round(valor, 2)