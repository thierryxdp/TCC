def fatorial (numero):
    '''Função que dado um número, calcula o fatorial desse número.
    int->str'''
    
    i=0
    r=() 
    fat = list(range(numero))
    elemento = len(list(range(numero)))
    sucessor = 1
    
    while i<len(list(range(numero))):
        elemento = elemento * sucessor
        if sucessor in fat:
            sucessor += 1
        i+=1
        
    return elemento//numero