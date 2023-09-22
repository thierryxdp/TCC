def media_matriz(matriz):
    '''
    Dado uma matriz de inteiros, não vazia, retorna a média dos elementos dessa matriz

    Uso:
   media_matriz(matriz)

    Entrada:
    - matriz (list): Matriz de informação

     Saída:
    - Retorna a média dos elementos de uma dada matriz. (float)
    '''

    j = 0
    soma = 0
    elementos = 0
    i = 0
    while i < len(matriz):
        c = sum(matriz[j])
        soma = soma + c
        d = len (matriz[j])
        j = j + 1
        elementos = elementos + d
        i = i + 1
    return round(soma/elementos,2)