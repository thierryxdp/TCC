def freq_palavras(frases):
    '''Dado uma frase, retorna um dicionário onde cada palavra é uma chave e o valor é o número de vezes que a palavra aparece
    strin->dict'''
    dicio={}
    frase=str.split(frases)
    
    for i in range(len(frase)):
        dicio['frase[i]']=list.count(frase,frase[i])
        return dicio