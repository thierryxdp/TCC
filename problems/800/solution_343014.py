def total(lista, itens):
    ''' Função que recebe uma lista de compras e retorna o preço
    total a ser pago'''
    'list,dict--->float'
    i=0
    
    resultado=dict.values(itens)
    produto=dict.keys(itens)
    while i < len(lista):
        if produto in lista:
            i=i+1
            print ('produto na lista')
        if produto not in lista:
            i=i+1
            print (produto)