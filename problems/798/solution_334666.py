def freq_palavras(frases):
    """funcao que recebe uma string e retorna um dicionario onde as chaves sao as palavras da string e os valores sao a quantidade de vezes que a palavra aparece;
       str->dict"""
    dicio={}
    frases=frases.split(" ")
    for i in range(len(frases)):
        if frases.count(frases[i])!=0:
            dicio[frases[i]]=list.count(frases,frases[i])
    return dicio