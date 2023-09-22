def freq_palavras(frase):
    chave=[]
    numero=[]
    palavra=str.split(frase)
    for i in palavra:
        qtd=list.count(palavra,i)
        list.append(chave,i)
        list.append(numero,qtd)
        a={i:qtd}
    return a