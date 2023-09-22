# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(c,p):
    """Dada uma lista de compras e um dicionario, retorna o valor total dos itens
    Entrada: lista, dict-->float"""
    i = 0.0
    for x in c:
        if x in p:
            i = i + dict.get(p,x)
    return round(i,2)