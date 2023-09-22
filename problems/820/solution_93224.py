def posLetra(frase,letra,n):
    '''Função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc) e retorna em que posição da string aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1'''
    frase2 = str.replace(frase,letra,"+",n-1)
    return str.find(frase2,letra)