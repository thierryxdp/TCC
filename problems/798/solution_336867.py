def freq_palavras(frases):
    "recebe uma string e retorna um dicionario onde cada palavra dessa string é uma chave e o valor é o número de vezes que tal palavra aparece"
    lista = [str.split(frases,' ')]
    dicionario = {}
    for palavra in lista:
        if palavra in dicionario:
            dicionario[elemento] += 1
        else:
            dicionario[elemento] = 1
    return dicionario