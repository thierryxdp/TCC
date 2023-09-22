def quant_palavras(frase):
    '''função que retorna o número de palavras de uma frase; str -> int'''
    if frase[0]==' ' and frase[-1]==' ':
        return (len(str.split(frase,' ')))-2
    if frase[0]== ' ':
        return (len(str.split(frase,' ')))-1
    if frase[-1]== ' ':
        return ((len(str.split(frase,' '))))-1
    else:
        return len(str.split(frase,' '))