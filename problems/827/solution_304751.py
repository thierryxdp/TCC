def qtd_divisores(n):
    """Conta quantos divisores um número tem
    	int -> int
        Parameters:
        n: Número a ser analisado
        
        Returns:
        Quantidade de divisores do número n
    """
    cont = 0
    
    for i in range(1,n+1):
        if n%i == 0:
            cont = cont+1
            
    return cont