def primo(numero):
    '''Função que, dado um número inteiro positivo, verifica se é um número primo ou não;
    int->bool'''
    contador=0
    for indice in range(1,numero+1):
    	if numero%indice==0:
            contador=contador+1
    if contador==2:
        return True
    return False