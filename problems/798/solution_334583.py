def freq_palavras(frases):
    frases = frases.split()
    resultado = {}
    for palavra in frases:
      	if palavra in resultado:
            resultado[palavra]+=1
      	else:
            resultado[palavra]=1
    return resultado
'''dado uma frase, a funcao retorna um dicionario contendo 
a quantidade de ocorrencia de cada frase
str->dict'''