def freq_palavras(frases):
    '''dada uma string retorna um dicionário onde cada palavra dessa string seja uma chave
    e tenha como valor o número de vezes que a palvra aparece
    str->dic'''
    dic={}
    palavras str.split(frases)
    for palavra in palavras:
        cont=list.count(palavras, palavra)
        dic[palavra]=cont
    return dic