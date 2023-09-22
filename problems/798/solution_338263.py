def freq_palavras(frases):
    """
    Essa função recebe uma string e retorna um dicionario onde cada 
    palavra dessa string é uma chave e o valor é o número de vezes 
    que a palavra aparece
    Parametro de entrada: str
    Valor de saida: dic
    """
    palavras = str.split(frases)
    dic ={}
    for pa in palavras:
        p1=frases.count(pa)