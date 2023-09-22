# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def total(lista,dicionario):
    total_compra = 0
    for i in lista:
        total_compra += dicionario[lista]
    return total_compra