def freq_palavras(frase):
'''funcao recebe frase e retorna dicionario'''
'''str--> dict'''
palavras = frase.slipt()
dict1 = {}
counter = 0
for elementos in palavras:
    dict1[palavras[counter]] = palavras.count(palavras[counter])
    counter += 1
return dict1