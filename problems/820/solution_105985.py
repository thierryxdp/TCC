def posLetra(string, letra, n):
    """ função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc). A função retorna em que posição da string aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1
string -> string"""
    ocorrencia=string.find(letra)
    while ocorrencia>=0 and numero>1:
        ocorrencia=string.find(letra,ocorrencia+1)
        numero-=1
    return ocorrencia