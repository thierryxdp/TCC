def  posLetra(string, letra, n):
    '''
        Função que indica a ocorrência desejada da letra passada na entrada;
        string => int
    '''
    pos = -1
    qtd = 0

    for i in range(len(string)):
        if(string[i] == letra):
            qtd = qtd + 1
            if(qtd == n):
                pos = i
                break

    return pos