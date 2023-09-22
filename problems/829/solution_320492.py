def soma_h (N):
    '''Funcao que calcula a soma de H .
    int->float'''
     
    'H = 1/1 + 1/2 + 1/3 + 1/4 + .... + 1/N'
    
    lista = []
    denominador = 1
    numerador = 1 
    
    for denominador in range(1, N+1):
        if 1%denominador != 0:
            denominador += 1
            
        list.append(lista, 1%denominador)
    return round(sum(lista),2)