def faltante(n):
    '''Essa função ao receber como valor de entrada uma lista com N - 1 inteiros numerados de 1 a N, descobre qual é o número inteiro deste intervalo está faltando.'''
    '''list -> int'''
    i=0
    resultado= 1
    while i<leb(n):
     if n[i]==i+1:
        resultado=n[i]+1
     i=i+1
    return resultado