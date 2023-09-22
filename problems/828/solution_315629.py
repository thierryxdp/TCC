def primo(n):
    """
    Calcula quantos divisores o numero n possui;
    int -> bool
    """
    div = []
    tamanho_div = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            div = div + [i]
            tamanho_div = tamanho_div + len(div)
    if tamanho_div == 1:
        return True
    else:
        return False