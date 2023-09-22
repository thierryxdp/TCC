def faltante(lista):
    '''dada uma lista com N − 1 inteiros numerados de 1 a N,
 descobre qual número inteiro deste intervalo está faltando'''
    lista=sorted(lista)
    estagio=0
    while estagio<len(lista):
        if not lista[estagio]==estagio+1:
            return estagio+1
        estagio+=1
    return estagio