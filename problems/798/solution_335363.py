def freq_palavras(frases):
    """recebe uma string e retorna um dicionario onde
    cada palavra sera uma chave e tenha como valor o
    numero de vezes que essa aparece
    str -> dict"""
    palavras = list(str.split(frases," "))
    dici={}
    for palavra in palavras:
        dici[palavra]=list.count(palavras,palavra)
    return dici