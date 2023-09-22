def fatorial(numero):
    '''função que, dado um numero, retorna seu fatorial.
    int -> int''' 
    
    i = 1
    fat = 1
    
    while i <= numero:
        fat = fat*i   
        i += 1
    return fat