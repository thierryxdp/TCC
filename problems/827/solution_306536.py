def lista_n(n):
    lista=list(range(n+1))
    for i in range(n+1):
        if n % i == 0:
            return True
        else:
            return False
def qtd_divisores(n):
    return len(list(filter(lista_n,list(range(1,n+1)))))