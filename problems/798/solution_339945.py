def freq_palavras(frases):
    ''' Esta função retorna o número de vezes que uma palavra aparece em uma frase'''
    dici={}
    palavras=str.split(frases)
    for palavra in palavras:
        cont=list.count(palavras,palavra)
        dici[palavra]=cont
    return dici