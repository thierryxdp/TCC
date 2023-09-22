def qtd_divisores(n):
   '''Calcula a quantidade de divisores de um numero n
   int -> int'''
   
    qtd_divisores=0
    
    for divisor in range(1,len(n)+1):
        if n%divisor==0:
            qtd_divisores+=1
    return qtd_divisores