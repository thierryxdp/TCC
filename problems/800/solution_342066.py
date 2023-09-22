def total(lista, produtos):
    '''função calcula total da lista de compras
    de acordo com os preços do dicionário
    list, dict--> float'''

    contador = 0  #inicia contador em zero
    total = 0  #inicia valor total das compras em zero
    
    for elementos in lista:  #para cada elemento da lista de compras
        if lista[contador] in produtos:  #se elemento da lista de compras estiver disponível no dicionário de produtos
            total += produtos[lista[contador]]  #incrementa total com preço do produto(preço é uma chave do dicionário)
            contador += 1  #incrementa contador

    return round(total, 2)  #retorna valor arredondado pra 2 casas decimais