def primo(n):
    """Função que dado um inteiro 'n' retorna True se ele for primo
    e False se não for o caso;
    int -> bool"""
    for e in range(2,n+1):
        if n != e  and n%e == 0:
            return False
    return True