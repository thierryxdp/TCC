def qtd_divisores(n):
    """Dado um numero, mostra quantos divisores ele possui. int>int"""
    resultado=0
    for i in range(1,n+1):
        if n%i==0:
            resultado+=1
    return resultado