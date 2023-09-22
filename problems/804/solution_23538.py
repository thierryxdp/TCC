def filtra_pares(a):
    '''Funçao que recebe uma tupla com quatro elementos 
    inteiros como parâmetro, e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original, na 
    mesma ordem em que se encontravam
    tuple->tuple'''
    lista = []
    for i in a:
        if type(i) != int:
            lista = []
            break
        elif i%2 == 0:
            lista.append(i)
            tuple(lista)
            else:
                ()