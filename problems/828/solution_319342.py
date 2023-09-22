# Primo
def primo(numero):
    """Essa função recebe um numero e avalia se ele e um numero primo ou não
    int -> bool"""
    qt_div = []
    for i in range(1,numero+1):
        if numero%i == 0:
            qt_div.append(i)
    if len(qt_div) <= 2:
        return True
    else: 
        return False