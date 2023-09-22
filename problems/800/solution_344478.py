# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total (lista_compra, produtos):
    valor_total = 0 
    for produto in lista_compra:
        valor_total+=produtos[produto]
    return round (valor_total,2)