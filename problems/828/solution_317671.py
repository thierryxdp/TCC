def primo(n):
    """função que recebe um numéro e retorna um valor boleano
    int->bool"""
    divisores=0
    for i in range(int(n/2)):
        if n%(2+i)!=0:
            divisores=True
        if n%(i+2)==0:
             return False
    return divisores