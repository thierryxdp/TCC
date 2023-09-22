def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um numero
    para retornar em que posição da string a ocorrência da
    letra está.
    str, str, int -> int'''
    p=string.find(letra)
    while p>=0 and i>=1:
        p=string.find(l,p+1)
        i=i-1
    return p