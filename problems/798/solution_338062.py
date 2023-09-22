def freq_palavras(frases):
    """"essa função recebe um string e retorna um dicionário em que cada palavra dessa string é uma chave e tem como valor o numero de vezes que a palavra aparece
    string_>dict"""
    freq={}
    n=0
    separados=frases.split(' ')
    for i in range(len(separados)):
        n=separados.count(separados[i])
        freq[separados[i]]=n
    return freq