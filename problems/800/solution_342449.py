def total(compras:list,dicionario:dict):
    #A soma começa com 0, soma é um acumulador
    soma=0
    #Verifica os produtos na lista de compra
    for produto in compras:
        #Vê se o produto está contido no dicionário
        if produto in list(dicionario.keys()):  
            #A somo vai ser igual ao valor da chave do produto
            soma+= dicionario[produto]
    return round(soma,2)