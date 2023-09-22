def freq_palavras(frases):
    """função que recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece;string-->dicionario"""
    frase1 str.split(frases)
    frequencia = {}
    for palavra in frase1:
        quantidade = list.count(frase1,palavra)
        frequencia[palavra] = quantidade
    return frequencia