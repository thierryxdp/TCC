def qtd_divisores(n):
    """Conta quantos divisores um número tem
    OBS:Função tirada do ex passado;int->int"""
    contador=0
    for i in range(1,n+1):
        if n%i==0:
            contador=contador+1
    return contador

def primo(n):
    """Dado um número inteiro positivo, verifica se este número
    é primo ou não;int->bool"""
    if n>=2:
        return qtd_divisores(n)>1
    else:
        return false