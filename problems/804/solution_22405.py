def filtra_pares(tuplas):
    '''Função que retorna os elementos pares de uma tupla de quatro elementos, em ordem;
    entrada: int, int, int, int;
    saída: tuple;
    '''
    sopares=()
    if (tuplas[0]%2==0):
        sopares= sopares + (tuplas[0])
    if (tuplas[1]%2==0):
        sopares= sopares + (tuplas[1])
    if (tuplas[2]%2==0):
        sopares= sopares + (tuplas[2])
    if (tuplas[3]%2==0):
        sopares= sopares + (tuplas[2])
    return sopares