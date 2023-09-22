def primo(numero):
    '''Funcao que, dado um numero de entrada (numero), retorna se ele é primo ou nao; int -> bool'''
    div=2
    while div<numero:
        div+=1
        if numero%div==0:
            return False 
        else:
            return True