def filtraMultiplos (lista, n):
    '''Função recebe uma lista e um número inteiro e retorna 
    os multiplos desse valor N presentes na lista
    list, int -> list'''
    
    multiplos = list()
    i = 0
    resposta =list()
    while (i<len(lista)):
        if (lista[i]% n == 0):
            multiplos +=(lista[i],)
                 
        i += 1
        
    return multiplos