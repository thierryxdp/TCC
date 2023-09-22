def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um numero
    para retornar em que posição da string a ocorrência da
    letra está.
    str, str, int -> int'''
    p=0
    i=0
    while string.count(letra)>=numero:
        if string[i]==letra:
            i=i+1
        p=p+1
    else:
        i=-1 
    return i