def qtd_divisores(n):
    """ Função que conta quantos divisores um número tem.
    int, int->int """
    qtd=0
    x=int(n**0.5)
    for i in range(2,(x//1)+1):
        if n%i==0:
            qtd=qtd+i
        if n%i==0 and n/i!=i:
            qtd=qtd+(n/i)            
    return int(qtd)