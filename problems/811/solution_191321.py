def colchao(cama, h, l):
    '''
    Dada uma lista com as dimensões A,B,C de uma cama em centimetros, ordenada
    da menor para a maior, e dois inteiros H e L, que são a altura e a largura da
    porta em centimentros retorna um booleano que diz que o colchao passa ou não
    pela porta.
    [int, int, int], int, int -> Bool
    '''
    if cama[2]<h and cama[1]<l:
        return True
    else:
        return False