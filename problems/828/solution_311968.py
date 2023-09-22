def primo(numero):
    """Função que dado um numero inteiro positivo, retorna se ele é primo ou não.
    int --> bool"""
    
    for x in range numero:
        if numero % x != 0 :
               return True
        else :
               return False