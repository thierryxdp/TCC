def primo(n):
    """funcao que recebe um numero inteiro e retorna se ele é ou não primo
	int -> bool"""
    
    primo = 0 
    for x in range(1,n):
        if n % x == 0:
           primo = x + 1
    if primo == 2:
        return True
    else:
        return False