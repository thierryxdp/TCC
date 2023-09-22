def primo(numero):
    "função que retorna se um número é ou não primo"
    "int -> bool"
    divisores=[]
    qt_divisores=0
    divisores_possiveis=list(range(1,numero+1))
    primo=False
    
    for divisor in divisores_possiveis:
        if numero%divisor==0:
            divisores.append(divisor)
            
    if len(divisores) <=2:
        primo=true
        return primo
    else:
        primo=false
        return primo