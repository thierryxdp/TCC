def total(lista_de_compras,produtos):
    soma=0
    for produto in lista_de_compras:
        preco_item=produtos[produto]
        soma+=preco_item
    return soma