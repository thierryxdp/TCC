def freq_palavras(frases):
    """função que retorna um dicionário com a quantidade de 
    vezes que uma palavra aparece em uma determinada frase
    str=>dict"""
    listaFrases = frases.split(" ")
    dicionarioF={}
    for i in range(len(listaFrases)):
        dicionarioF[listaFrases[i]]=listaFrases.count(listaFrases[i])
	return dicionarioF