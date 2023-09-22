def faltante(lista):
    '''Entrada: O parâmetro de entrada é uma lista L de tamanho N − 1 contendo números inteiros (não repetidos) de 1 a N.
Saída: A sua função deve retornar o número inteiro x que pertence ao intervalo [1, N] mas que não pertence a lista de entrada L
Exemplos:

Entrada: [3,1]; Saída: 2
Entrada: [1,2,3,5] ; Saída: 4
Entrada: [2,4,3] ; Saída: 1
int->int'''
    i=1
    while i<99:
        if i not in lista:
            return i
        i+=1