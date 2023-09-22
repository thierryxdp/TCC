def freq_palavras(frase):
    chave=[]
    numero=[]
    dicionario={}
    palavra=str.split(frase)
    for i in palavra:
        novo=dict.copy(dicionario)
        qtd=list.count(palavra,i)               
        novo[i]=qtd
    return novo