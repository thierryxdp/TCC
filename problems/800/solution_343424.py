def total(lista,produtos):
    '''funcao que dada uma lista de compras e um dicionario contendo o preço
    de cada produto, retorna o valor todato dos intes da lista que estejam disponiveis;
    list, dict => float'''
    
    contador = 0
    resultado = 0
    
    for i in lista:
        if lista[contador] in produtos:
            resultado = resultado + produtos[lista[contador]]
            contador = contador+1
    return round(resultado,2)