def qtd_divisores(n):
    '''a seguinte função irá retornar quantos
    divisores um numero irá possuir'''
    divisores = [] 
    qtdivisores = 0 
    divisorespossiveis= list(range(1,n+1))
    
    for divisor in divisorespossiveis:
        if n%divisor == 0: 
            divisores.append(divisor)
    qtdivisores = len(divisores) 
    return qtdivisores