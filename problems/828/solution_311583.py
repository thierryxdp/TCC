def primo (n):
    """Função que retorna "True" caso um número seja primo e "False" caso
    não seja."""
    """int--bool"""
    lista=list(range(2,n))
    for elemento in lista:
        if n%elemento==0:
            return True
        else:
            return False