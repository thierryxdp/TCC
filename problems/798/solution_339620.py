def freq_palavras(frases):
    '''recebe uma string e retorna um dicionário com as palavras e suas respectivas frequências dentro da string
    str -> dict
    '''
    dicionario = {}
    lista = str.split(frases)
    for palavra in lista:
        qtd = list.count(lista, palavra)
        dicionario[palavra] = qtd
    return dicionario