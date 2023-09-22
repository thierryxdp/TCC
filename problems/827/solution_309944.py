def qtd_divisores(n):
    """Função que conta quantos divisores um número tem; int -> int"""
    lista=[]
    divisores=list(range(1,n+1))
    for numero in divisores:
        if n%numero==0:
            lista.append(numero)
    return len(lista)