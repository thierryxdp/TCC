def freqpalavras(frase):
    """Recebe uma string e retorna um dicionário contendo 
    todas as palavras da string e quantas vezes elas se 
    repetem na frase.
    Assinatura: str -> dict"""
    dic={}
    fc=str.split(frase)
    for palavra in fc:
        vzs = fc.count(palavra)
        dic[palavra]=vzs
    return dic