def total(lista,produtos):
    '''Dados uma lista de compras e um dicionário contendo os
    produtos existentes em uma loja e seus respectivos valores,
    a função retorna o valor da compra de todos os itens comuns à
    lista e ao dicionario. list,dict --> float'''
   
    total = 0
   
    for item in lista:
        if item in produtos:
            total=total+produtos[item]
           
    return round(total,2)