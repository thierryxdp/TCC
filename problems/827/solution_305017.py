#---------------------EXERCICIO 2---------------------

def qtd_divisores (numero):
    '''Retorna quantos numeros divisores
        o numero inserido tem
       int -> int'''
    
    divisores = 1 #qtd divisores do numero até o momento
    
    for contador in range(1,numero, divisores):
        divisores += (numero%contador == 0)
            
    return divisores