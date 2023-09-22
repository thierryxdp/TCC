def freq_palavras(frase):
    dicionario={}
    palavra=" "
    palavra=str.split(frase)
    for i in palavra:
        qtd=str.count(frase,i)
        dicionario=dicionario+i+':'+qtd
    return qtd