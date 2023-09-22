def qtd_divisores(n):
    """
    Função recebe um número n como parametro, e retorna a quantidade de divisores
    que este número possui.
    int -> int
    """
    divisores=0
    for i in range(1,n+1):
        if (n%i)==0:
            divisores+=1
    return divisores