def posLetra(frase, letra, pos):
    '''Função que recebe uma string, uma letra
    e um número que indica a ocorrência (local) da letra'''
    'str---->int'
    t=len(frase)
    p=str.index(frase,letra)
    q=str.count(frase,letra)
    i=0
    a=0
    if 1==pos:
        return p
    elif q<pos:
        return -1