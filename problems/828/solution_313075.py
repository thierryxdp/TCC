def primo(int_pos):
    '''Verifica se o inteiro positivo é um numero primo
    int -> Bool'''
    lista = []
    for x in range(2,int_pos):
        if int_pos % x == 0:
            lista.append(x)
    if len(lista) == 0:
        return True
    else:
        return False