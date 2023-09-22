def freq_palavras(frase):
    '''dada a variante, ele recebe a str. e retorna um dicionario explicitando quantas vezes as palavras da frase foi repetida.str->dict.'''
 palavras = str.split(frase)
 dicionario = {}
 for i in palavras:
   if i in dicionario:
     dicionario[i] += 1
    else:
      dicionario[i] = 1
 return dicionario