def fatorial(numero):
    '''função que recebe um numero como entrada e retorna o valor do 
    fatorial deste numero; int->int'''
    
    i=numero
    valor=1
    
    while i>0:
        valor=valor*i
        i=i-1
    return valor