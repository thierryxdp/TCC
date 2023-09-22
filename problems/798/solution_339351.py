from collections import Counter

def freq_palavras(frases):
    texto = [];
    palavra_procurada = {};
    dicionario = Counter(texto)
    
    for palavra in palavra_procurada:
        print (palavra + " " + str(dicionario[palavra])
               if palavra in palavra_procurada else 0)