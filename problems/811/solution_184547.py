def colchao(lista, Hporta,Lporta):
    """ Função que calcula se o colchão passa ou não da porta, dada uma lista com os tamanhos, e os numeros inteiros da altura e da largura da porta"""
    dim1,dim2,dim3=lista
    if dim1<=Hporta and dim2<=Lporta:
        return True
    if dim1<=Hporta and dim3<=Lporta:
        return True
    if dim2<=Hporta and dim3<=Lporta:
        return True
    if dim1<=Lporta and dim2<=Hporta:
        return True
    if dim1<=Lporta and dim3<=Hporta:
        return True
    if dim2<=Lporta and dim3<=Hporta:
        return True
    else:
        return False