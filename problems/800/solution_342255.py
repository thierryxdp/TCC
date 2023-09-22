def total(compras,produtos):
    ''' função que retorna o valor dos produtos que estão disponiveis
    list, dict -> float'''
    valores = 0
    for i in range(len(compras)):
        valores = valores + produtos[compras[i]]
    return round(valores,2)
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis