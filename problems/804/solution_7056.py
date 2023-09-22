def filtra_pares(tupla):
    '''Função que recebe uma tupla com quatro números inteiros e retorna uma nova tupla
    contendo apenas os números pares da tupla original;
    tuple -> tuple'''
    x = ()
    if (tupla[0]%2) == 0:
        x=x+(tupla[0],)
    elif (tupla[1]%2) == 0:
        x=x+(tupla[1],)        
    elif (tupla[2]%2) == 0:
        x=x+(tupla[2],)
    elif (tupla[3]%2) == 0:
        x=x+(tupla[3],)
    return x