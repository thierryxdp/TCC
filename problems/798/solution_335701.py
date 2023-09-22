def freq_palavras(frases):
    """retorna um dicionario com a frequencia
    de cada palavra da frase.
    string->dict"""
    D={}
    indice=0
    palavra=frases.split()
    for palavra in frases:
        D(frases[indice])=palavra.count(palavra[indice])
        indice= indice + 1
        return D