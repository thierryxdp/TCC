# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,dicionario):
    '''retorna o valor dos produtos de uma lista de compra
    list, dict -> float'''
    total = 0
    for elemento in lista:
        if elemento in dicionario:
            total += dicionario[elemento]
    return round(total,2)