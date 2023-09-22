def fatorial (n):
    ''' dado um numero n retorna seu valor fatorial;
    int->int'''
    listap_fatorar= list(range(1,n))
    list.reverse (listap_fatorar)
    valor= n
    indice=0
    while indice < len (listap_fatorar):
        valor = valor * listap_fatorar[indice]
        indice+=1
    return valor