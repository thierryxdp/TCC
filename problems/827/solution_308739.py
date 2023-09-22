def qtd_divisores(n):
    """ Funçao que conte quantos divisores um numero tem """
    if n==0 or n<0:
        return 0
    lista=list(range(1,n+1))
    for i in lista:
        if n%i == 0:
            divisores = list.count(lista,i)
            return divisores