def freq_palavras(frases):
    ''' Recebe um texto e retorna um dicionario onde cada palavra desse texto é uma chave e o seu valor é o numero de vezes que ele se repete.
string->dict'''
    str.strip(frases)
    acumulador={}
    frases=str.split(frases)
    for palavra in frases:
        if palavra not in acumulador:
            y=list.count(frases,palavra)
            acumulador[palavra]=y
            
    return acumulador