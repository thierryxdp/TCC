def primo(n):
    """
    Função que dado um inteiro positivo retorna um valor
    booleano se for primo.(True se sim. False se não.)
    """
    qtd_divisores=0
    lista_divisores=list(range(2,n))
    for i in lista_divisores:
        if n%i==0:
            return False
        else:
            return True