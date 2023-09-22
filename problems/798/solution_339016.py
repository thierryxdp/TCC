def freq_palavras(frases):
    '''função em que dada uma string, retorne um dicionário onde 
    cada palavra dessa string seja uma chave e tenha como valor o número
    de vezes que a palavra aparece list -> dici'''
    dici = [] 
    for palavra in frases:
        if frases in dict(palavra):
            dici = dici + [palavra]
    return dict.key(dici)