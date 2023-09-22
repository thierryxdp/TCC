# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compras, produto):
    contagem = 0
    valor_total = 0
    limit = len(lista_compras)
    while contagem < limit:
        valor_total += produtos[lista_compras[contagem]]
        contagem += 1
        valor_total = round(valor_total, 2)
    return valor_total