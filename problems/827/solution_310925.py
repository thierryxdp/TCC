def qtd_dividores(num):
    '''Função que conta quantidade de divisores que um núemro tem;
    Recebe um número;
    Retorna a quantidade de divisores que esse número tem.'''
    divisores = []
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador = contador + 1
            list.append(divisores, i)
    return len(dividores)