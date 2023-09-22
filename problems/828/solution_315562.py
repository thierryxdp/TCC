def primo(numero):
    '''Função que recebe um número inteiro positivo e verifica
    se ele é ou não primo. int->bool'''
	resposta = 0
    for i in range (1,numero+1):
        if numero%i==0:
            resposta = resposta +1
    if resposta>2:
        return False
    else:
        return True