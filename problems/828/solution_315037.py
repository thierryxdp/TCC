def primo(n):
    """Função que retorna um valor booleano, indicando se o número inserido é
    primo ou não"""
    n_divisores=0
    for d in range(1,int((n+1)/2)):
        if n%d==0:
            n_divisores=n_divisores+1
    return n_divisores==1