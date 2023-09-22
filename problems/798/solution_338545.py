def freq_palavras(frases):
    """Função que recebe uma frase e retorna um dicionário contendo
a quantidade de cada palavra; str -> dict"""
    palavras=str.split(str.lower(frases))
    vezes=0
    dicionario={}
    for item in palavras:
        vezes=str.count(" "+str.lower(frases)+" "," "+item+" ")
        dicionario[item]=vezes
    return dicionario