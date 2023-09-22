def primo(p):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    n = int
    i = 0 
    for count in range(2,n):
        if (n % count == 0):
            return True
     
        if(i==0):
            return True
        else:
            False