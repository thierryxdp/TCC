#---------------------EXERCICIO 2---------------------

def qtd_divisores (numero):
    '''Retorna quantos numeros divisores
        o numero inserido tem
       int -> int'''
    
    divisores = 0
    
    for contador in range(1,numero+1, divisores+1):
        divisores += (numero%contador == 0)
            
    return divisores