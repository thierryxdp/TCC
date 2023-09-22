def total(lista_de_compras, produtos):
    """Essa função recebe uma string e um dicionário, 
   é escolhida quais termos do dicionario serao 
   selecionados de acordo com a  propria string. Por fim 
   serão pegos os valores do dicionario e somados.
   
   assinatura: string, dict ----> float
   """
    preco=0
    for produto in lista_de_compras:
        if produto in lista_de_compras:
            preco+=produtos[lista_de_compras[lista_de_compras.index(produto)]]
    return round(preco,2)