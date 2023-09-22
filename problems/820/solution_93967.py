def posLetra(frase,l,n):
    '''Dado uma frase, uma letra e um número respectivamente.
    retorna a posição da string na qual a ocorrencia da letra está.
    str,str,int --> int'''
    a = list(frase)
    b = list.count(a,l)
    y = 0
    x = list.index(a,l,y)
    proximo = 1
    if n > b or b == 0:
        return -1
    while proximo < n:
        y = x+1
        x = list.index(a,l,y)
        proximo = proximo + 1
    return x