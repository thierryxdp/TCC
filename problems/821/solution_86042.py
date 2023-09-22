def fatorial(n):
    '''Função que dado um número (n) como entrada, retorna o fatorial desse número.
       parâmetro de entrada:int
       valor de retorno:int'''
    contador=n
    fatorando=1
    while contador>1:
        fatorando=fatorando*contador
        contador=contador-1
    return fatorando