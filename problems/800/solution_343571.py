def total(lista_de_compras,produtos):
    '''dadas as variantes, ele o que tem no dicionario e retorna a soma dos valores da lista. list,dict->int.'''
    soma=0
    for produto in lista_de_compras:
        preco_item=produtos[produto]
        soma+=preco_item
    print(soma)