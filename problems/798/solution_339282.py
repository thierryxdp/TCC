def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionário onde cada
    palavra da string é uma chave e o valor é o número de vezes em que
    a palavra aparece
    str->dict'''
    
    x=frases.split(' ')
    lista_palavras=[]
    lista_freq=[]
    
    for palavras in x:
        list.append(lista_palavras,palavras)
        list.append(lista_freq,lista_palavras.count(palavras))
        
    return lista_palavras,lista_freq