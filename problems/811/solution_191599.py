def colchao(medidas,h,l):
    '''Funcao que dado as medidas do colchao e da porta 
    retorna se sera possivel ou nao passar com o colchao pela
    porta
    Parametros:
    int
    Saida: bool
    '''
    m=medidas[1:]
    if m[0]< h:
        return True
    if m[1]< l:
        return True
    else:
        return False