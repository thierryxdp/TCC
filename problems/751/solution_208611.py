def quant_palavras(frase):
    '''função que recebe uma frase(string) e retorna o número de palavras dessa
frase, sem contar os espaços vazios entre as palavras e nos extremos da frase;
string->int'''

    frase2= str.strip(frase)
    lista= str.split(frase)
    final=str.join('',lista)

    return len(final)