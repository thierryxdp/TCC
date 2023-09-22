def qtd_divisores (n):
    ''' função que calcula e retorna a quantidade de divisores
        que um número possui
        [int-->int]'''
    
    divisores = 0
    
    if n < 0 :
        return divisores 
    
    else :
        FATORIAL = list(range(n+1))
        list.remove(FATORIAL,0)

        for numero in FATORIAL: 
            if n % numero == 0 :
                divisores += 1
        return divisores