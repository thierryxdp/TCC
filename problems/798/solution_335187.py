# A função recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave
# e tenha como valor o número de vezes que a palavra aparece
# string-->dict
#
def freq_palavras(frases):
    i=0
    dicionario={}
    lista=frases.split()
    while i<len(lista):
        dicionario[lista[i]]=p.count(lista[i])
        i=i+1
    return dicionario