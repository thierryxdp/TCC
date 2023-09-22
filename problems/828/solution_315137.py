def primo(numero):
    '''Funcao que, dado um numero de entrada (numero), retorna se ele é primo ou nao; int -> bool'''
    i=0
    div=2
    while div<numero:
        if numero%div==0:
            retorno=False
        else:
            retorno=True
        div=div+1
    return retorno