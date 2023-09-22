def freq_palavras(frases):
    '''recebe uma string e retorna um dicionário com as palavras e suas respectivas frequências dentro da string
    str -> dict
    '''
    dicionario = {}
    lista = str.split(frases)
    i = 0
    while (i < len(lista)):
        palavra = lista[i]
        qtd = list.count(lista, palavra)
        dicionario[palavra] = qtd
        i += 1
    return dicionario