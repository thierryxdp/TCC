def eh_quadrada(matriz):    
'''
A função recebe uma matriz e verifica se é uma matriz quadrada(matriz vazia é considerada quadrada)
retornando em caso afirmativo True e caso contrario False.
list->bool
'''
    if len(matriz)!=0:
        if len(matriz)==len(matriz[0]):
            return True
        return False
    return True