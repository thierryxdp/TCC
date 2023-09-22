def total(lista,mercado):
    '''
Função que recebe uma lista de compras e um dicionario
contendo o preços de cada produto disponível, e retorna o valor total dos itens da 
lista que estejam disponíveis nesta loja.

list, dict-->float
    '''
    
    total=0
    for i in range(len(lista)):
        total=total+mercado[lista[i]]
          
    return round(total,2)