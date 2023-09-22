# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(ls, produtos):
    ''' list dict > int
    Dada uma lista de compras (ls), retorna o valor total 
    da compra desses produtos segundo os valores indicados 
    no dicionário produtos'''

    r = []

    for p in ls:
        r.append(produtos[p])

    return round(sum(r),2)