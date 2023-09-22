def primo(n):
    """funcao que recebe um numero inteiro e retorna se ele é ou não primo
	int -> bool"""
    
    for primo in range(2,n):
        if n % primo == 0:
            return False
        else: 
            return True