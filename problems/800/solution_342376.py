def total(lista,preço):
    "recebe uma lista de produtos e um dicionario com os produtos e preço"
    "retorna o preço total da lista. entrada:float,str. saida:float"
    total=0
    for x in lista:
        if x in preço:
            total=total+preço[x]
    return round(total,2)