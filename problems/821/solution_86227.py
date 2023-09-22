def fatorial(numero):
    '''Essa funcao recebe 'numero' que irah multiplicando com
       a variavel fat a medida que ele eh decrescido, ateh chegar
       ao numero 1, momento onde o decrecimo termina e o valor
       fatorial eh obtido.
       (int -> int)'''
    fat = 1
    while numero > 0:
        fat *= numero
        numero -= 1
    return fat