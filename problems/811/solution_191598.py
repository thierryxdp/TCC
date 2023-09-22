def colchao(medidas,h,l):
    '''Funcao que dado as medidas do colchao e da porta 
    retorna se sera possivel ou nao passar com o colchao pela
    porta
    Parametros:
    int
    Saida: bool
    '''
    m=medidas[0:]
    if m[0]< h:
        return True
    else:
        return False