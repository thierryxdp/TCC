def freq_palavras(frases):
    "Retorne uma string e retorne um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece; str-> dici"
    f=frases.split()
    d={}
    for i in f:
        d[i]=f.count(i)
    return d