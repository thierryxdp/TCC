def freq_palavras(string):
    "Função que ao receber uma string de entrada, retorna um dicionário com as substrings e o número de ocorrências de cada. str --> dict"
    lista=str.split(string)
    dicio={}
    for palavra in lista:
        if palavra not in dicio:
            dicio[palavra]=1
        else:
            dicio[palavra]=dicio[palavra]+1
    return dicio