def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionário onde cada 
    palavra da string é uma chave e tenha como valor o número de vezes
    que essa palavra aparece.
    entrada:string
    saída:dicionário'''
    d={}
    frases=str.split(frases,' ')
    for i in range(len(frases)):
        if frases[i] not in d:
            d[frases[i]]=list.count(frases,frases[i])
    return d