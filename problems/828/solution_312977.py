def qtd_divisores(n):
    """funcao que calcula a quantidade de divisores de um determinado numero;int->int"""
    divisores=0
    for i in range(1,n+1):
        if n%i==0:
            divisores=divisores+1
    return divisores

def primo(n):
    """funcao que determina se um dado numero e primo; int->"""
    if qtd_divisores(n)==2:
        return True
    else:
        return False