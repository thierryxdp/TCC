conta_numero(numero, matriz):
    ''' Essa função retorna o quantas vezes um número inteiro aparece
    numa matriz de inteiros;
    int,list -> int. '''
    resultado = 0
    if len(matriz) == 0:
        return resultado
    for l in range(0, len(matriz)):
        if numero in matriz[l]:
            resultado += matriz.count([l],numero)
            return resultado