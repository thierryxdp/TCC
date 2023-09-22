def fatorial(n):
     '''função que dado um número 'n' calcula o fatorial deste número
        int->int'''
     fatorial=1
     while n>0:
         fatorial=fatorial*n
         n=n-1 
     return fatorial