def freq_palavras(frases):
    '''Função que conta quantas vezes cada palavra da frase se repete.
    retorna um dicionario com a relaçao palavra:repetições
    string -> dict'''
    lista = str.split(frases)
    d = {}
    for i in lista:
        d[i] = list.count(lista,i)
        
    return d