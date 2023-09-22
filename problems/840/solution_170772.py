def bolos(a,b,c):
    """função que dados a quatidade "a" de xic. de farinha, "b" de ovos e "c" de colheres de sopa de leite, calcula e retorna a quantidade exata de bolos que se pode fazer"""
    if ((a/2==int)and(b/3==int)and(c/5==int)):
        return min(a,b,c)
    else:
        return (0)