def freq_palavras(frases):
    '''a partir de uma string, retorna um dicionário com as palavras da string como chave e o número de vezes que cada palavra aparece como valor
str-->dict'''
    str.split(frases)
    for i in frases:
        return dict(i:str.count(i))