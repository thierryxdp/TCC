def repetidos(x):
    '''Função que retorne o número de vezes que o elemento
    da lista é igual ao número anterior. list-->int'''
    respost=0
    t=0
    while t<(len(x)-1):
    if x[t] == x[t+1]:
        resposta +=1
	t+=1
    return  resposta