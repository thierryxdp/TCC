def primo(n):
    """ Função que dado como entrada um número inteiro positivo n, verifique
    se este número é primo ou não e retorna um valor booleano, True para números
    primos e False para números que não são primos.
    int -> bool.
    """
    x = list(range(2,n))
    lista = []
    for numero in x:
        if n%numero !=0:
            lista += [numero]
            len(lista)
    if len(lista)>0:
        return False
    elif len(lista) == 0:
        return True