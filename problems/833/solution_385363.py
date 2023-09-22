def conta_numero(numero,matriz):
    '''
    Dado um numero e uma matriz retorna quantas vezes o numero aparece na matriz

    Uso:
   conta_numero(numero,matriz)

    Entrada:
    - numero (int): Número inteiro
    - matriz (list): Matriz de informação

     Saída:
    - Retorna quantas vezes um dado número repete-se na matriz de informação. (int)
    '''
    qnt = 0
    j = 0
    i = 0
    while i < len(matriz):
        c = list.count(matriz[j], numero)
        qnt = qnt + c
        j = j+ 1
        i = i + 1
    return qnt