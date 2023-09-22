def qtd_divisores(n):
    '''funçao que retorna o númedor de divisores de um número:int->int'''
    cont = 0 
   for x in range (1,n+1):
       if n % x == 0:
            cont += 1
   return cont