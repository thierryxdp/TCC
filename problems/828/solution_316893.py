def primo(p):
    """Funçao que dado o número n, retorna se é um número primo ou não """
    for i in range(3,p):
        if p%i==0 or p!=1 or p<2 or p%2==0:
            return False 
        if p//1==0 or p//p==0:
            return True