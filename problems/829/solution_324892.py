def soma_h(N):
    '''função que recebe N e retorna o valor H com N termos
int->float'''
    lista=list(range(1,N+1))
    soma=[]
    for i in lista:
        soma.append(1/i)
    return round(sum(soma),2)