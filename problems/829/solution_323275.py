def inv(x):
    '''
    Recebe um valor x e retorna o inverso 
    multiplicativo do mesmo, ou seja, eleva a -1.
    '''
    return x**-1

def soma_h(n):
    '''
    Recebe um valor n, atribui um contador k e uma soma s.
    Repete até que k seja igual a n. Ele recebe o inverso
    de k e soma este valor em s. Após isso, soma 1 em k.
    Por fim, arredonda o valor e retorna este valor arredondado.
    '''
    k = 1; s = 0
    while k <= n:
        s += inv(k)
        k += 1
        
    return round(s,2)