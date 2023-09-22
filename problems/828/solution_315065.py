def primo (n):
    """Função que dado um número inteiro n retorna um valor booleano"""
    """int->bool"""
    if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
        return True
    else:
        return False