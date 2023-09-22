def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um numero
    para retornar em que posição da string a ocorrência da
    letra está.
    str, str, int -> int'''
    p=string.find(letra)
    while p>=0 and numero>1:
        p=string.find(letra,p+1)
        numero=numero-1
    return p