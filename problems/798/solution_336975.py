def freq_palavras(frases):
    #separa cada item da frase em uma lista
    frases=frases.split()
    #Gera um dicionário
    dicionario={}
    #Gera uma chave pra cada palavra da frase
    for palavra in frases:
        #define as chaves como 0
        dicionario[palavra]=0
    #Soma 1 ao valor da chave a cada vez que aparece a palavra
    for palavra in frases:
        dicionario[palavra]+=1
    return dicionario