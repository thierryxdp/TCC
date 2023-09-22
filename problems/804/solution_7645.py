def filtra_pares(a):
    '''funcao que recebe uma tupla com 4 numeros inteiros e retorna uma nova tupla contendo apenas os elementor pares;tuple-->tuple'''
    l = []
    for i in a:
        if i%2 == 0:
            l.append(i)
                            
    return (l)