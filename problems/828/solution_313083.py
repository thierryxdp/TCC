def primo(n):
    """a função identifica os numeros como primo, caso não seja retorna False"""
    mult=0
    for count in range(2,n):
        if (n % count == 0):
            mult +=1
    if (mult==0):
        return True
    else:
        return False