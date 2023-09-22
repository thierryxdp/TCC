def qtd_divisores(numero):
    '''Funcao que retorna a quantidade de divisores que um numero tem, sendo esse numero o valor de entrada; int -> int'''
    quantidade=0
    div=1
    while div<=numero:
        if numero%div==0:
            quantidade=quantidade+1
        div=div+1
    return quantidade