def quant_palavras(frase):
    '''função que recebe uma frase(string) e retorna o número de palavras dessa
frase; string->int'''

    frase2= str.strip(frase)
    lista= str.split(frase2)
    

    return len(lista)