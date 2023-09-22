def eh_quadrada(matriz):
    """Dada uma matriz, retorna com true caso seja quadrada 
e false caso não seja.
list -> bool"""
    if len(matriz)==len(matriz[0]):
            return True
    else: 
        return False