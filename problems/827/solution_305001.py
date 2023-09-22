def divisores (numero):
    '''Função que retorna o total do número de divisores que um número tem, dado esse número como 
    valor de entrada.
    int -> int '''
    soma = 0
    lista = list(range(1,numero+1))
    for i in lista:
        if numero % (lista[i-1]) == 0:
            soma = soma + 1
    return soma