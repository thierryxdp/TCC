def primo(n):
    """
    Calcula quantos divisores o numero n possui;
    int -> bool
    """
    boleano = 0
    div = []
    tamanho_div = 0
    for i in range(1,n/2+1):
        if n%i == 0:
            div = div + [i]
            tamanho_div = tamanho_div + len(div)
            if tamanho_div == 2:
                boleano = True
            else:
                boleano = False
    return boleano