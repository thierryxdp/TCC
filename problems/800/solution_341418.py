def total(compras,produtos):
    """função que retorna o valor total das compras a serem feitas
    list,dict->float"""
    soma=0
    for produto in compras:
        soma=soma + produtos[produto]
    return round(soma,2)