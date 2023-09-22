# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
'''Soma o valor dos produtos de uma lista se estiver em um discionário.
list, dict --> float
'''
def total(ls,d):
    soma = 0
    for i in ls:
        soma += d[i]
    return round(soma,2)