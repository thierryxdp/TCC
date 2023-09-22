def posLetra(frase,letra,n):
    '''Função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra e retorna em que posição da string aquela ocorrência da letra está; str, str, int -> str'''
    i=0
    indice=0
    while i<len(frase):
        x=str.find(frase,letra)
        indice=indice+x
        i=i+0
    return indice