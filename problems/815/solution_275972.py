def  insere(lista_numero,n):
    '''
    Dada uma lista ordenada de numeros 
    e um numero inteiro n, a função inclui
    o n na posição correta, de tal maneira 
    que a lista contimnue ordenada
    list, int --> list
    '''
    lista_numero.insert(0,n)
    return  sorted(lista_numero)