def primo(numero: int):
    '''função que dado um número inteiro positivo verifica se esse número
    	é primo ou não e retorna um valor booleano'''
    for n in range(2,numero):
        if numero%n==0:
            return False
    else:
        return True