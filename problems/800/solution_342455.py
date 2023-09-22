def total(compras:list,dicionario:dict):
    soma=0
    for produto in compras:
        if produto in list(dicionario.keys()):
            soma+= dicionario[produto]
    return round(soma,2)