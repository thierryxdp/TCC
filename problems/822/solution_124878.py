def repetidos(lista):
    '''função que dada uma lista como dado de entrada devolve quantas vezes um número aparece duas vezes seguidas nessa lista;list->int'''
    i=0
    r=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            r=r+1
        i=i+1
    return r