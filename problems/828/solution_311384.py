def primo(n):
    """Função que dado um inteiro 'n' retorna True se ele for primo
    e False se não for o caso;
    int -> bool"""
    for e in [2,3,5,7]:
        if n != e  and n%e == 0:
            return False
    return True