def freq_palavras(frase):
    '''Dada uma string, retorna um dicionário onde cada palavra dessa string 
    seja uma chave e tenha como valor o número de vezes que a palavra aparece;
    string -> dict {string: int}'''

    dicionario = {}

    for palavra in str.split(frase):
        if palavra not in dicionario.keys():
            dicionario[palavra] = 1
        else:
            dicionario[palavra] += 1

    return dicionario