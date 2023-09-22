def freq_palavras(text):
#Dado uma determinada frase a função retorna um dicionnario contendo o numero de vezes que a palavra aparece, string -> dict.
    palavras = []
    for n in text.split():
        palavras = palavras + [n, ]
    
    valores = []
    for j in palavras:
        valores = valores + [palavras.count(j), ]

    return dict(zip(palavras, valores))