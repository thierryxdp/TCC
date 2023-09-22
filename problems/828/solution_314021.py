def primo(n):
    """
    Função que dado um inteiro positivo retorna um valor
    booleano se for primo.(True se sim. False se não.)
    """
    qtd_divisores=0
    for i in range(1,n+1):
        if n%i==0:
            qtd_divisores+=1
    if qtd_divisores==2:
        return True
    else:
        return False