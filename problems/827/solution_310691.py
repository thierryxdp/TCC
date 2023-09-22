def qtd_divisores(x):
#Dado um numero inteiro a funcao retorna a quantidades de divisores deste numero int -> int
    divisores = ()
    for num in range(1,x+1):
        if x%num == 0:
            divisores = divisores + (num ,)
    
    return len(divisores)