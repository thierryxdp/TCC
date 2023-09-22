# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, dicio):
    '''e recebido uma lista de compras e um dicionario com os precos
    e e retornado o valor da compra de acordo com os itens existentes
    no dicionario
    list, dict -> float'''
    
    valor = 0
    
    for i in lista:
        if i in dicio:
            valor+=i
    return valor