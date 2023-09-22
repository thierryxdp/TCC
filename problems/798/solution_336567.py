def freq_palavras(frase):
    dicionario=[]
    palavra=str.split(frase)
    for i in palavra:
        dicionario=dicionario+i
        qtd=list.count(palavra,i)
        dicionario=dicionario+qtd
    return qtd