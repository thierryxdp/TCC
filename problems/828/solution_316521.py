def primo(x):
    """funcao que dado um numero retorna se ele e primo ou nao; int->bool"""
    for y in range(1,int(x/2)+1):
        if (x%y==0) and (y>1):
            return False
    return True