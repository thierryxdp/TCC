def fatorial (numero):
    ''' funcao que dado um numero, calcula e retorna o seu fatorial
int -> int'''
    fat = 1
    for i in range(numero):
        fat = fat*(i+1)
    return fat