#---------------------EXERCICIO 2---------------------

def qtd_divisores (numero):
    '''Retorna quantos numeros divisores existem
       int -> int'''
    
    divisores = 0
    
    for contador in range(1,numero+1):
        if numero%contador == 0:
            divisores += 1
            
    return divisores