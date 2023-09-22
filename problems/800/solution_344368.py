# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compra, produtos):
    valor_total = 0
    for produto in lista_compra:
        if produto in produtos == True:
            valor_total+=dict.value(produto)
    return valor_total