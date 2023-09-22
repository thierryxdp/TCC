def flitraMultiplos (lista1,n):
    '''função que recebe como entrada uma lista numérica (lista1) e 
    filtra quais os números dessa lista que são múltiplos de um número
    (n) de entrada. E deve retornar uma nova lista contendo apenas os 
    números que são múltiplos da lista de entrada;
    lista,int->lista'''
    i = 0
    lista_nova =[]
    while i<len(lista1):
        if lista1[i]%n==0:
            lista_nova = lista_nova+[lista1[i]]
        i = i+1
    return lista_nova