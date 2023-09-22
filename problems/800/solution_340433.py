def total(lista,dicionario):
    """ função recebe uma lista com as comprar que deseja fazer e um dicionário que tem os itens da loja como chave e o preço como valor
    retorna o valor total dos itens da lista que estejam disponíveis naquela loja
    
    entrada->list,dict
    retorna->float"""
    
    valor=0
 
    for i in range(len(lista)):
        if lista[i] in dicionario:
            valor= valor+ dicionario[lista[i]]
            
    retun valor