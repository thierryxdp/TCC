def bolos(a,b,c):
    '''A funcao retorna o numero de bolos que podem ser
feitos levando em consideracao as medidas de 2a, 3b e 5c
para que seja feito 1 bolo e so serao feitos bolos com o
numero exatos de medidas'''
    if (a%2==0)and(b%3==0)and(c%5==0):
        return (a+b+c)/10
    else:
        return(a+b+c)//10