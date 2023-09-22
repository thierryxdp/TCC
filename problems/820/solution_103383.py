def posLetra(frase,letra,n):
    '''Função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra e retorna em que posição da string aquela ocorrência da letra está; str, str, int -> str'''
    i = frase.find(letra)
    while i >= 0 and n > 1:
        i = frase.find(letra, i + 1)
        n -= 1
    return i