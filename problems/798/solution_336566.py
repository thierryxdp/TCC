def freq_palavras(frase):
    dicionario=[]
    palavra=str.split(frase)
    for i in palavra:
        
        dicionario=dicionario+i+list.count(palavra,i)
    return qtd