def colchão(cama, h, l):
    '''
    Dada uma lista com as dimensões A,B,C de uma cama em centimetros, ordenada
    da menor para a maior, e dois inteiros H e L, que são a altura e a largura da
    porta em centimentros retorna um booleano que diz que o colchao passa ou não
    pela porta.
    [int, int, int], int, int -> Bool
    '''
    if cama[0]>l and cama[1]>h:
        return False
    else:
        return True