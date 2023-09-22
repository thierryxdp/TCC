def total(compras:list,dicionario:dict):
    'recebe uma lista de compras e um dicionario com os preços de cada produto e retorna o valor a ser pago pela compra'
    soma=0
    for produto in compras:
        if produto in list(dicionario.keys()):
            soma+= dicionario[produto]
    return round(soma,2)