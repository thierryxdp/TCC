def soma_h(num):
    '''Essa função tem como objetivo somar um valor por 'num' vezes para
    saber o retorno de H.'''
    #int -> int -> int
    
    result = 0
    for i in range ((1),(num+1)):
        result += (1/i)
        
    return round(result,2)