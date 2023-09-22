def qtd_divisores(n):
    """A função retorna a quantidade de divisores naturais de um valor n de entrada.
    assinatura: int --> int
    """
    final=[]
    for i in range(1, n+1):
        if n%i==0:
            final.append(i)
    return len(final)