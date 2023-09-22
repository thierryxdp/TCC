def freq_palavras(frases):
    """funcao que dada uma string, retorna um dicionario onde cada palavra dessa str é uma chave e o seu valor é o numero de vezes que a palavra aparece
    str--->dict[str:int]
    dicionario={}
    frases=str.split(frases)
    for elem in range(len(frases)):
        qtd_vezes=list.count(frases,frases[elem])
        if frases[elem] not in dicionario:
            dicionario[frases[elem]]=qtd_vezes
    return dicionario