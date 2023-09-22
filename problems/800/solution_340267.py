# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(l,d):
    """Função que recebe uma lista e um dicionário,
    e retorna a soma dos itens da lista:
    list, dict -> float"""
    d = dict()
    l = list()
    
    for l in d.items():
        if l not in d:
            d[l] = 1
        else:
            d[l] = d[l] + 1
    d = sum(d[l])
    return d