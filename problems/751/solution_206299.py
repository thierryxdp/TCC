def quant_palavras(frase):
    '''Dada uma frase, retorna a quantidade de palavras que existem na frase.
    string -> int'''
    semEspaco = str.strip(frase)
    return str.count(semEspaco, ' ') + 1