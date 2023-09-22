# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,produtos):
    total = 0
    for itens in lista:
        if itens in produtos:
            total = produtos[itens] + total

    return round(total,2)