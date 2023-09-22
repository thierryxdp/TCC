def primo(num):
    '''Função que retorna atraves de um booleano se um número inteiro positivo é primo.
    int->bool'''
    qtd_divisores=0
    for divisor in range(2,num):
        if num%divisor==0:
            qtd_divisores=+1
    return qtd_divisores==0