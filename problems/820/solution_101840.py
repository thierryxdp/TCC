def posLetra(s,letra,numero):
    '''Função que recebe uma string, uma letra e um numero
    para retornar em que posição da string a ocorrência da
    letra está.
    str, str, int -> int'''
    p=s.find(letra)
    while p>=0 and i>1:
        p=s.find(letra,p+1)
        i=i-1
    return p