def freq_palavras(frases):
    """
	Função recebe uma string e retorna um dicionário onde cada palavra dessa
    string seja uma chave e tenha como valor o número de vezes que a palavra
    aparece.
    str -> dict
    """
    lista=str.split(frases," ")
    dicio={}
    for i in lista:
        freq=list.count(lista,i)
        dicio[i]=freq
    return dicio