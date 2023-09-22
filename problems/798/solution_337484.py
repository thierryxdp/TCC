def freq_palavras(frases):
    '''função que receba uma string e retorna um dicionário onde cada palavra dessa string seja
    uma chave  como valor o número de vezes que a palavra aparece
    string->dicionário'''
    dicio={}
    frase=str.split(frases)
    i=0
    while i <len(frase):
        repetido=list.count(frase,frase[i])
        dicio[frase[i]]=repetido
        i=i+1
    return dicio