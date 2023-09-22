def f(a,b):
    return a[b]
def mapeia (f,a,ls):
    ret=[]
    for b in ls:
        list.append(ret,f(a,b))
    return tuple(ret)

def total(ls,a):
    '''Função que recebe uma lista de compras e um dicionário 
    contendo o preço de cada produto disponível e retorna o valor
    total dos itens da lista que estejam disponíveis nesta loja.
    assinatura: list, dict -> float'''
    return round(sum(mapeia(f,a,ls)),2)