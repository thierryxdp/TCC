def fatorial(n):
   """função que dado um número, retorna o fatorial deste
   int=>int""" 
    
    cont=1
    i=2
    while i<=n:
        cont = cont*i
        i+=1
    return cont