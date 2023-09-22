def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece; str -> dict'''
    frases=str.split(frases)
    i=0
    freq={}
    for palavra in frases:
        if palavra not in freq:
            freq[frases[i]]=list.count(frases,palavra)
        i+=1
    return freq