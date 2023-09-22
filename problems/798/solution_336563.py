def freq_palavras(frase):
    dicionario=[]
    palavra=str.split(frase)
    for i in palavra:
        qtd=str.count(palavra,i)
        dicionario=dicionario+i+qtd
    return qtd