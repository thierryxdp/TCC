def posLetra(string,l,n):
    '''Adicionar a documentação!'''
    x = 0 #contador e y é a posição
    for y in range(len(string)):

        if(string[y] == l):
            x += 1
            if (x == n):
                return y
    return -1