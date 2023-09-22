def total(lista_de_compras, produtos):
    """Essa função recebe uma string e um dicionário, 
   é escolhida quais termos do dicionario serao 
   selecionados de acordo com a  propria string. Por fim 
   serão pegos os valores do dicionario e somados.
   
   assinatura: string, dict ----> float
   """
    proximo=0
    soma=0
    while( proximo < len(lista_de_compras)):
        soma += produtos[lista_de_compras[proximo]]
        proximo+=1 
    return round(soma,2)