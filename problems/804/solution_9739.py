def filtra_pares(_t):
    ''' Retorna uma tuple com os elementos pares dos argumentos
    	(int, int, int, int) -> (,int)
        Explicação: Usa if com o operador % em cima do intereable para checar o resto da divisão por dois de cada elemento, 
        concatenando a uma tuple com o resultado'''
    ret = ()
    if _t[0] % 2 == 0:
        ret += (_t[0] ,)
    if _t[1] % 2 == 0:
        ret += (_t[1], )
    if _t[2] % 2 == 0:
        ret += (_t[2], )
    if _t[3] % 2 == 0:
        ret += (_t[3], )
    return ret