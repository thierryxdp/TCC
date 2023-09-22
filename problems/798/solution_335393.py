def freq_palavras(frases):
    ''' Recebe um texto e retorna um dicionario onde cada palavra desse texto é uma chave e o seu valor é o numero de vezes que ele se repete.
string->dict'''
    acumulador={}
    x=str.split(frases)
    for palavra in x:
        if palavra not in acumulador:
            y=str.count(frases,palavra)
            acumulador[palavra]=y
            
    return acumulador