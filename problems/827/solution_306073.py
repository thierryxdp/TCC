def qtd_divisores(numero):
    '''Função que conta quantos divisores tem um número
    int -> int'''
    
    divisores = 0
    
    for n in list(range(1,numero+1)):
        if (numero%n) == 0:
            divisores = divisores + 1
            
   return divisores