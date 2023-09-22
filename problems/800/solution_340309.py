# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(l,d):
    """Função que recebe uma lista e um dicionário,
    e retorna a soma dos itens da lista:
    list, dict -> int"""
    l1 = ()
    for l in d:
        if l not in d:
            d[l] = 1
        else:
            l1 = l1 + (d[l],)
            d[l] = d[l] + 1
           
    return sum(l for l in l1)
total(['a','b','c'],{'a':1,'b':2,'c':2,'d':1,'e':1,'f':1})