def filtra_pares(lista):
    ''' 
    Função recebe uma tupla contendo quatro elementos inteiros. 
    Retorna uma tupla contendo os elementos pares
    '''
    lista_par = [] 
    for par in lista:
        if par % 2 == 0:
            lista_par.append(par)
        else: 
            return ()
    return lista_par
# Exemplo de uso
lista = (1, 4, 2, 8) 
filtra_pares(lista)#Start your python function here