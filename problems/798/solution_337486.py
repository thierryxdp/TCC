def freq_palavras(frases):
    """Recebe uma frase e retorna um dicionario com todas as palavras citadas nessa frase e suas respectivas ocorrencias;
    	str -> dict"""
    dicio={}
    frases=str.split(frases,' ')
    for i in range(len(frases)):
        if frases[i] in dicio:
            dicio[frases[i]]+=1
        else:
            dicio[frases[i]]=1
    return dicio