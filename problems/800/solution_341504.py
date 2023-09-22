def total (compras, mercado):
    ''''retorna o valor de uma lista de compras(ldc) baseado em um dicionário
(mercado)'''
    valor = 0
    for i in compras:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis