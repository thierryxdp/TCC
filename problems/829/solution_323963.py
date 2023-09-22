def soma_h(n):
    '''função que calcula o somatório de frações com n termos;
        int=>float'''
    lista = [1]
    
    for i in range(2, n+1):
        lista = lista+[(i)**-1,]
    return round( sum(lista) ,2)