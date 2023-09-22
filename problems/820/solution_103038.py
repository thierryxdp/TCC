def posLetra(string,letra,n):
    ''' Essa função tem como objetivo contar quantas letras tem em uma
    stringer, dado um número de vezes que ele quer que ocorra, caso não
    aconteça, a resolução volta (-1).
    str,str,int -> int'''
    

    s = str.count(string)
    
    if  s < n:
        return -1