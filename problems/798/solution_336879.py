def freq_palavras(frases):
    " recebe uma frase e retorna um dicionario com as palavras e o numero de vezes que uma palavra aparece"
    d={}
    frases=frases.strip()
    frases=frases.split('')
    for palavra in frases:
        if palavra in d:
            d[palavra]=d[palavra]+1
        else:
            d[palavra]=1
    return d