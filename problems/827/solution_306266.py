def qtd_divisores(num):
    '''Conta e retorna quantos divisores um número(num) 
       passada por entrada tem;
       int -> int'''
    
    divisores = []
    
    for n in range(1,num+1):
        
        if num % n == 0:
            
            divisores.append(n)
            
    return len(divisores)