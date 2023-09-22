def freq_palavras(frase):
    dicionario={}
    novo=dict.copy(dicionario)
    palavra=str.split(frase)
    for i in palavra:
        qtd=list.count(palavra,i)
        novo[i]=qtd
    return novo