def freq_palavras (frase):

frase=frase.split()

dicionario={}

   for n in frase:

     dicionario[n]=list.count(frase,n)

   return dicionario