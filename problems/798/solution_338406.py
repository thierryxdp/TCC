# Recebe uma frase e retorna um um dicionário onde cada palavra da frase é uma frase e tem como valor o número de vezes que a palavra se repete.
# str --> dict
def freq_palavras(frases):
    palavras=str.split(frases,' ')
    dicionario={}
    for i in palavras:
        dicionario[i]=list.count(palavras,i)
    return dicionario