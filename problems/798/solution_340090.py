def freq_palavras(frase):
    dic = {}
    frase = str.split(frase,'')
    for letra in range(len(frase)):
        if frase[letra] in dic:
            dic[frase[letra]] += 1
        else:
            dic[frase[letra]] = 1
    return dic