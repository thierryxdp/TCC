def primo(numero):
    '''função que diz se um número é primo
    int --> boolean'''
    qtd=0
    for i in range(1,numero+1):
        if numero % i == 0:
            qtd=qtd+1
	if qtd == 2:
        return True
    else:
        return False