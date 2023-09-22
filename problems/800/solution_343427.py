def total(produtos_lista,precos_dict):
    '''
    Função que retorna o valor total dos itens no estoque, após receber na entrada
    uma lista de compras junto ao dicionário com a tabela de preços de cada produto no estoque.
    list,dict->float 
    '''
    total_preço=0
    contador=0
    
    while contador<len(lista):
        if produtos_lista[contador] in dict.keys(precos_dict):
            total_preco=total_preco+dict.get(precos_dict,produtos_lista[contador])
        contador=contador+1
    return round(total_preco,2)