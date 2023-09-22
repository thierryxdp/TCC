def primo(p):
    """Funçao que dado o número 'p', identifica se o mesmo é primo ou não;
int -> bool"""
    if p < 2 or p%2==0:
        return False
    if p == 2:
        return True
    for i in range(3,p // 2,2):
        if p%i == 0:
            return False
        else:
            return True