def total(lista_de_compras, produtos):
    """Essa função recebe uma string e um dicionário, 
   é escolhida quais termos do dicionario serao 
   selecionados de acordo com a  propria string. Por fim 
   serão pegos os valores do dicionario e somados.
   
   assinatura: string, dict ----> float
   """
    preço=0
    for produto in lista:
        if produto in lista_de_compras:
            preço+=produtos[lista_de_compras[lista_de_compras.index(produto)]]
    return round(preco,2)