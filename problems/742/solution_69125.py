def substitui(s,x,i):
	'''
    Funcao que retorna a string inserida mais um caracter
    s = string base
    x = string do caracter
    i = numero inteiro que esta no intervalo 0<i< len (s)
    str,str,int -> str
    '''
    if i>0 and i<len(s):
        return s + x
    else:
        return 'numero i é maior que o comprimento da string'