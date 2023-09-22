def freq_palavras(frases):
    """
    Função que recebe uma string e retorna um dicionário
    onde cada palavra dessa string é uma chave e tem como
    valor o número de vezes que a palavra aparece na frase
    """
    palavras=frases.split()
    dic={}

    for palavra in palavras:
        numero=palavras.count(palavra)
        dic[palavra]=numero
    return dic