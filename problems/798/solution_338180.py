def freq_palavras(frase):
 palavras = str.split(frase)
 dicionario = {}
 for i in palavras:
   if i in dicionario:
     dicionario[i] += 1
   else:
      dicionario[i] = 1
 return dicionario# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis