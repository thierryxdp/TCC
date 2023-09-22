def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário onde cada palavra dessa string é uma chave e tem como valor o número de vezes que aparece.
    str -> dict'''
    frase = str.split(frases)
    dict = {}
    contador = 0
    
    for contador in range(len(frase)):
        lista = list.count(frase,frase[contador])
        dict [frase[contador]] = lista
        contador = contador + 1
    return dict