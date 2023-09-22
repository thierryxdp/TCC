def freq_palavras(frases):
    texto = [];
    palavra_procurada = {};
    
    for palavra in palavras_procuradas:
        print (palavra + " " + str(dicionario[palavra])
               if palavra in palavra_procurada else 0)