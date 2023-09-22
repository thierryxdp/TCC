import palavra_procurada

def freq_palavras(frases):
    texto = [];
    palavra_procurada = {};
    
    for palavra in texto:
        if palavra in palavras_procuradas:
            count = 1
            if palavra in dicionario:
                count = int(dicionario[palavra].split(' ')[-1]) + 1;
                dicionario[palavra] = palavra + " " + str(count)
                
                for palavra in palavras_procuradas:
                    if palavra not in texto:
                        dicionario[palavra] = palavra + " " + str(0) 
                        for chave in dicionario:
                            print (dicionario[chave])