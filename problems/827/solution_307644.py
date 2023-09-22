def qtd_divisores(n):
    div = ()
    i =  1
   
    while i <= n:
        if n % i == 0:
            div = div + (1)
        i = i + 1 
    return div