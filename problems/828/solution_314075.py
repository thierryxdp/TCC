def primo(n):
    """
    Função que dado um inteiro positivo retorna um valor
    booleano se for primo.(True se sim. False se não.)
    """
    qts_divisoes=0
    lista_divisores=list(range(2,n,2))
    for i in lista_divisores:
        if n%i==0:
            qts_divisoes+=1
    if qts_divisoes==0:
        return True
    else:
        return False