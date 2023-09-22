def primo(numero):
    """Essa função diz se um número é primo ou não
    int -> bool"""
    qt_div = []
    for x in range(1,numero+1):
        if numero%x == 0:
            qt_div.append(x)
    if len(qt_div) <= 2:
        return True
    else: 
        return False