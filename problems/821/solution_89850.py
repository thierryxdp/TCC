def fatorial(numero):
    '''
        recebe um numero e calcula o seu fatorial
        entrada: inteiro
        saida: inteiro
    '''
    if numero == 0:
        return 1
    else:
        decre = 1
        controle = numero - decre
        resultado = numero
        while controle > 0:
            resultado = resultado * controle
            controle = controle - decre
        return resultado