def primo (numero):
    '''Função que dada um número inteiro positivo,
    retorne um booleano afirmando ou negando se
    ele é primo ou não;
    entrada: int
    saída: bool'''
    if numero != 0 & numero != 1:
        if numero > 3:
            for i in range(2, numero):
                if numero % i == 0:
                    return False
        return True
    return False