def total(compras,custos):
    ''' A partir de uma lista de compras e um dicionário contendo todos
    os preços de uma loja, retorna o valor da lista de compras pra ser comprada
    (arredondado com 2 casas decimais);
    list,dict->float'''
    valor_final=0
    for produto in compras:
        if produto in custos:
            valor_final+=custos[produto]
    return round(valor_final,2)