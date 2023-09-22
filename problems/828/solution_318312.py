def primo(numero):
    """Recebe um número inteiro positivo, verifica se ele é primo
    
    int -> bool"""
    v = 0
    for x in range(2, numero):
        if numero%x == 0:
            verificador = 1
    if v == 1:
        return False
    if v == 0:
        return True