def primo(numero):
    cont = 0
    for indice in range(2,numero):
        """ Percorrendo os intervalos entre 2 e o número anterior à entrada """
        if numero % indice == 0:
            """ Caso encontre números que dividem a entrada sem resto, retorna que
            False, caso não econtre, o retorno de fora do laço faz retorna Verdadeiro """
            return False
            break
            
    return True