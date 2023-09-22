def soma_h(N):

    '''A funcao recebe o numero n como entrada e retorna a soma 1/1+ 1/2 + 1/3 +...1/n

int->float'''

    lista=list(range(1,N+1))

    soma=[]

    for i in lista:

        soma.append(1/i)

    return round(sum(soma),2)