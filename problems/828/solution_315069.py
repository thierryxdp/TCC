def primo (n):
    """Função que dado um número inteiro n retorna um valor booleano"""
    """int->bool"""
    if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0 and n%11!=0 and n%13!=0 and n%17!=0 and n%21!=0 :
        return True
    else:
        return False