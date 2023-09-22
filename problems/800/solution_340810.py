# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(l,d):
    """Função que recebe uma lista e um dicionário,
    e retorna a soma dos itens da lista:
    list, dict -> int"""
    l1 = 0
    for m in l:
        if m in d:
            l1 += d[m]
    return round(l1, 2)