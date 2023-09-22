def filtra_pares(tupla):
    '''Função que recebe uma tupla com quatro números inteiros e retorna uma nova tupla
    contendo apenas os números pares da tupla original;
    tuple -> tuple'''
    return (x for x in tupla if x%2==0)