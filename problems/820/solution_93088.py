def posLetra(frase,letra,n):
    '''Função que, dada uma frase, uma letra e um número, retorna a enésima posição da letra.
    str,str,int --> int'''
    i = 0
    if frase.count(letra)+ frase.count(str.upper(letra))< n:
        return -1
    while frase[0:i].count(letra)+ frase[0:i].count(str.upper(letra))< n:
        i = i + 1
    return i - 1