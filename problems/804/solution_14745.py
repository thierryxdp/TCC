def filtra_pares (tup):
    '''função que retorna uma tupla apenas com os elementos
    pares dados como entrada, dado como entrada uma tupla 'tup'
    de quatro elementos inteiros'''[
        par = ()
        if tup [0]%2==0:
        	par=par+(tup[0],)
        if tup [1]%2==0:
        	par=par+(tup[1],)
        if tup [2]%2==0:
        	par=par+(tup[2],)
        if tup [3]%2==0:
        	par=par+(tup[3],)
        return par