def repetidos(lista_numeros):
    '''retorna o numero de vezes que um numero da lista se repete duas vezes seguidas
    list --> int'''
    i=0
    repeticoes=0
    while i < len(lista_numeros):
        if lista_numeros[i]==lista_numeros[i-1]:
            repeticoes=repeticoes+1
        i=i+1
    return repeticoes