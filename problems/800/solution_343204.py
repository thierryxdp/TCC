def total(lista_de_compras,produtos):
    ''' função que, ao receber o preço de cada produto disponivel em uma loja retorna o valor
        total dos itens da lista disponivel nessa loja
        list, dict ---> float '''
    valor = 0
    a = valor
    for produto in lista_de_compras:
        valor = produtos[produto]
        a = a + valor
    return round(a,2)