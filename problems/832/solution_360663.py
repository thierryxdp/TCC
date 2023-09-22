def eh_quadrada(m):
    ''''dada uma matriz em forma de lista somos capazes, 
    com essa funçao de detreminar por meio de expereçoes 
    booleanas se a matriz dade é quadrada.
    temos que se quadrada, a expresao bool retornada sera 
    True, e se nao quadrada, a expreçao retornada sera
    False
    lista-->bool'''
    numeroLinhas=len(m)
    if len(m)==0:
        return True 
    else:
        numeroColunas=len(m[0])
        if numeroColunas==numeroLinhas:
            return True
        else:
            return False