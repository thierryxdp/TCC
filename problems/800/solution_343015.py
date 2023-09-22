# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compras, precos):
    '''
    Essa função recebe uma lista de compras e um dicionário com o preço de cada produto
    e retorna o valor a ser gasto no mercado
    
    list, dict -> float
    '''
    total=0
    for produto in lista_compras:
        total=total+precos[produto]
    return round(total,2)