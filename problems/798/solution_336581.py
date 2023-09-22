def freq_palavras(frase):
    dicionario={}
    palavra=str.split(frase)
    for i in palavra:
        qtd=list.count(palavra,i)
        dicionario=i
    return dicionario