def qtd_divisores(n):
   '''Calcula a quantidade de divisores de um numero n
   int -> int'''
   qt_divisores=0
    for divisor in range(1,n+1):
        if n%divisor==0:
            qt_divisores+=1
    return qt_divisores