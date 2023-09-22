def colchao(medidas, H, L):
    '''
    	Funcao que recebe as medidas do colchao, a altura
        e a largura da porta e retorna se e possivel o
        colchao passar pela porta
        medidas, altura, largura em centimetros
        medidas devem estar em ordem descrescente
        list, int, int -> bool
    '''
    if medidas[1] <= H:
        return True
    elif medidas[1] <= L:
        return True
    elif medidas[2] <= H:
        return True
    elif medidas[2] <= L:
        return True
    else:
        return False