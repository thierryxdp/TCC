def qtd_divisores(numero):
    '''Função que retorna a quantidade de divisores de um inteiro dado
    int -> int'''
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    return contador