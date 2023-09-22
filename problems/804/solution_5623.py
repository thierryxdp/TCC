def filtra_pares(a,b,c,d):
    '''Função que recebe uma tupla com quatro números e retorna uma nova tupla
    contendo apenas os números pares da tupla original;
    int, int, int, int -> tuple'''
    tupla = [a,b,c,d]
    return [x for x in tupla if x%2==0]