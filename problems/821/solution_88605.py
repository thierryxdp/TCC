def fatorial(numero):
    '''Função que retorna a fatoração de um número de entrada: int -> int'''
    fatoracao = 1
    indice = 1
    while indice <= numero:
        fatoracao *= indice #fatoracao = fatoracao*indice
        indice += 1 #indice = indice + 1
    return fatoracao