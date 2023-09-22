def colchao(medidas,h,l):
    '''Funcao que dado as medidas do colchao e da porta 
    retorna se sera possivel ou nao passar com o colchao pela
    porta
    Parametros:
    int
    Saida: bool
    '''
  	if medidas[1]< h:
        return True
    if medidas[2]< l:
        return True
    else:
        return False