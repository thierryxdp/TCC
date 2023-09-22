def freq_palavras(frase):
    chave=[]
    numero=[]
    dicionario={}
    palavra=str.split(frase)
    for i in palavra:
        qtd=list.count(palavra,i)
        list.append(chave,i)
        list.append(numero,qtd)
        #a={i:qtd}
        novo=dict.copy(dicionario)
        novo[i]=qtd
    return novo