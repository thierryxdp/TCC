def qtd_divisores(n):
    """função que conte quantos divisores um numero tem, este numero sera passado como entrada 
    int -> int"""
    contador=[]
    contador=0
   
    for divisor in n:
        if n%divisor == 0: 
            contador = contador + 1 
        return contador