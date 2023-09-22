def primo(numero):
    """retorna se o numero informado é primo
    int->bol"""
    indice=0
    for elemento in range(1, numero+1):
        if numero%elemento==0:
            indice=indice + 1
        if indice>2:
            return false
        else:
            return True