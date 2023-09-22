def posLetra(s,letra,n):
    '''Retorna a posição da ocorrência 'n' da letra de entrada
       na string 's';
       str, str, int -> int'''
    qtdLetra=count(s)

    if n>qtdLetra-1:
        return -1

    count=0
    while count<qtdLetra:
        pos=s.index(letra)
    return pos