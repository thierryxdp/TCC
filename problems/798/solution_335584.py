def freq_palavras(frase):
    """retorna um dicionario com a frequencia
    de cada palavra da frase.
    string->dict"""
    D={}
    indice=0
    for palavra in frase:
        D(frase[indice])=palavra.count(frase[indice])
        indice= indice + 1
    return D