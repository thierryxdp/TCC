def primo(numero):
    '''Funcao que, dado um numero de entrada (numero), retorna se ele é primo ou nao; int -> bool'''
    i=0
    div=2
    while div<=numero:
        if div<numero and numero%div==0:
            return False 
        elif div<numero and numero%div!=0:
            return True