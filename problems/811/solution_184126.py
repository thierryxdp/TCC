def colchao(medidas,H,L):
    '''A funcao recebe uma lista com as dimensoes de um colchao (em centimetros, ordenadas
    da menor para a maior) e dois inteiros H e L (que correspondem a, respectivamente,
    altura e largura da porta em centimetros) e retorna se é possível ou nao passar o
    colchao pela porta.
    Parametro de entrada: list(int,int,int),int,int
    Valor de retorno: bool'''
    if medidas[2]<=H or medidas[2]<=L:
        return True
    if medidas[1]<=H or medidas[1]<=L:
        return True
    else:
        return False