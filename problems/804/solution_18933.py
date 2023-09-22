def filtra_pares(a):
    '''Função que recebe uma tupla com 4 elemetos inteiros como
    parametro e retorna uma nova tupla contendo apenas os elementos
    pares da tupla original, na ordem dada
    '''
    num1, num2, num3, num4 = a
    tupla = tuple()
    if num1%2==0:
        tupla += (num1,)
    if num2%2==0:
        tupla += (num2,)
    if num3%2==0:
        tupla += (num3,)
    if num4%2==0:
        tupla += (num4,)
   
    return tupla