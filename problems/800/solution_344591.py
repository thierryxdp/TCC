# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,produtos):
    total = 0
    x = 0
    while x < len(lista):
        if lista[x] in produtos:
            total = produtos[lista[x]] + total
        x = x + 1

    return round(total,2)