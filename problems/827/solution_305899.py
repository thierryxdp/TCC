def qtd_divisores(numero):
    """função que conter quantos divisores um numero tem, este numero sera passado como entrada
    int -> int"""
    
    divisores = list()
    for n in numero:
        if (numero%n == 0):
            list.append(divisores, n)
            
   	return tuple(divisores)