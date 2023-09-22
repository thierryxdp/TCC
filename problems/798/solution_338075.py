def freq_palavras (frase):
    '''Recebe um string e retorna um dicionário cujas chaves são 
    as palavras e cujos valores representam o número de vezes em que
    cada palavra aparece;
    str -> dict {str:int}'''
    palavras=[]
    palavras=str.split(frase,' ')
    frequencias={}
    for item in palavras:
        chaves=dict.keys(frequencias)
        if item not in chaves:
            frequencias[item]=1
        else:
            frequencias[item]=frequencias[item]+1     
    return frequencias