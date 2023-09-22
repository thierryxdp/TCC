def freq_palavras (frases):
    '''Dada uma string, retorne um dicionário que cada
       letra tenha uma chave e tenha como valor o número 
       de vezes que a palavra apareça;
       string -> dict'''
    dic = {}
    aux = frases.split()
    for palavra in aux:
        if palavra in aux:
            dic [palavra] = list.count(auxiliar,palavra)
    return dic