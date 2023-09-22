def qtd_divisores(numero):
    """função que conter quantos divisores um numero tem, este numero sera passado como entrada
    int -> int"""
    count = 0
   
    for n in range(1, numero+1):
        if (numero%n == 0):
            count = count + 1
            
    return count