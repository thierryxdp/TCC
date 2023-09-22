# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(listadecompras, produtos):
    '''A função retorna a soma do preço dos produtos de uma lista de compras
    list, dicionario -> float'''
    soma = 0
    i = 0
    while i<len(listadecompras):
        soma = soma + produtos[listadecompras[i]]
        i = i+1
    return round(soma, 2)