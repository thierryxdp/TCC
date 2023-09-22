def primo(nip):
    """retorna se um numero inteiro positivo é primo ou nao.
    int->bool"""
    for x in range(2,nip):
        if nip % x ==0:
            return False
    else:
            return True