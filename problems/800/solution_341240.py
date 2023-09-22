def total(lista_compras,produtos):
    soma=0
    "função que recebe uma lista de compras e um dicionario que contendo"
    "o preço de cada produto disponível em uma determinada loja"
    " e retorna o valor total dos itens da lista"
    "list,dict->float"
    for i in range(len(lista_compras)):
        if lista_compras[i] in produtos:
            soma=soma+ produtos.get(lista_compras[i])