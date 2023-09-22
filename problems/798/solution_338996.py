def freq_palavras(frases):
    ''' Esta função retorna o número de vezes que uma palavra aparece em uma frase; str->dici'''
    dici={}
    palavras=str.split(frases)
    for palavra in palavras:
        cont=str.count(frases,palavra)
        dici[palavra]=cont
    return dici