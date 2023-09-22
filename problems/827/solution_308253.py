def qtd_divisores(numero):
    "função que retorna o total de divisores que um numero possui"
    "int -> int"
    divisores=[]
    i=0
    divisores_possiveis=list(range(1,numero+1))
    
    for divisor in divisores_possiveis:
        if numero%divisor==0:
            divisores.append(divisor)
    i=len(divisores)
    return i