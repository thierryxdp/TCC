def total(l=[],d={}):
    '''
       funcao que recebe uma lista de compras 
       e um dicionario contendo o preço de cada
       produto disponivel em uma determinada loja, e 
       retorna o valor total dos intens disponiveis nesta loja
       list,dict->int
    ''' 
    cont=0.0
    for caractere in l:
        cont+=d[caractere]
    return round(cont,2)