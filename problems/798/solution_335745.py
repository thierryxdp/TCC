def freq_palavras(frases):
    """função que recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece;string-->dicionario"""
    frase_sep str.split(frases)
    frequencia = {}
    for palavra in frase_sep:
        quantidade = list.count(frase_sep,palavra)
        frequencia[palavra] = quantidade
    return frequencia