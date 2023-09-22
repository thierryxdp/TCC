def primo(n):
    '''Funcao que dado um numero como parâmetro, calcula todos os divisores do numero
em questão. Apos isso, ele retorna como valor booleano dizendo se o numero da entrada
é primo,percorrendo na ideia do numero primo ter apenas 2 divisores, 1 e ele mesmo.
    int - > bool'''
    divisores = 0
    for numero in range(1, n + 1):
        if n % numero == 0:
            divisores = divisores+1
            
    return divisores==2