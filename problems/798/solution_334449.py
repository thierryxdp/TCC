def freq_palavras(frases):
     '''recebe uma string e retorna um dicionário onde 
cada palavra dessa string é uma chave e 
tenha como valor o número de vezes que
a palavra aparece.'''
        str.split(frases)
        dicio={}
        for word in frases:
            if word not in dicio:
                dicio[word]=1
            if word in dicio:
                dicio[word]=dicio[word]+1
        return dicio