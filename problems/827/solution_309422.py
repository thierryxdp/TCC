def qtd_divisores(numero):
    ''' dado um número qualquer calcula a quantidade de divisores
    inteiros um número tem
    int --> int '''
    
    i = 1
    divisores = 0
    
    while i <= numero:
        if i % numero == 0:
            divisores += 1; i += 1        
        else:
            i +=1
    return divisores