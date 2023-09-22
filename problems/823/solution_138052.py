def faltante(lista):
    '''função que dada uma lista com N-1 inteiros numerados
    de 1 a N, retorna o número inteiro que está faltando
    dentro deste intervalo
    list -> int
    '''
    contador = 0
    ordenada = sorted(lista)
    while contador < len(lista):
        if contador+1 == ordenada[contador]:
            contador += 1
        else:
            return contador + 1
    return contador + 1