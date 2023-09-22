def soma_h(n):
    '''Função que recebe um inteiro N e retorna H=1/1+1/2+1/3+...+1/N'''
    soma=0
    #looping que faz as somas da divisoes ate o chegar no valor de N
    for i in range(1,n+1):
        soma+=1/i
    #arredonda o valor em 2 casa decimais
    somaH=round(soma,2)
    return somaH