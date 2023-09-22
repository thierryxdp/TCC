def primo(n):
    """função que recebe um número inteiro positivo e retorna True se esse número for primo ou False se não for um número primo
	int -> bool"""
    
    cont = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
            
    if cont == 2:
        return True
    
    else: 
        return False