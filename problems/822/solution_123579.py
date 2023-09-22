def repetidos (lista_num):
    '''Função que dada uma lista aleatória de números (lista_num)
    retorna quantas vezes um elemento da lista é igual ao elemento 
    anterior a ele.
    list[int]-> int'''
    i=0
    repetidos=0
    
    while i< len(lista_num):
        if lista_num[i] == lista_num[i-1]:
            repetidos= repetidos+1
        i=i+1
        if len(lista_num)==2 and lista_num[0] == lista_num[1]:
            repetidos=1
            
    return repetidos