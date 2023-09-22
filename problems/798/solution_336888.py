def freq_palavras(frases):
    "recebe uma string e retorna um dicionario onde cada palavra dessa string é uma chave e o valor é o número de vezes que tal palavra aparece"
    lista = [str.split(frases,' ')]
    dicionario = {}
    for palavra in lista:
        if not palavra in list(dict.keys(dicionario)):
            dicionario[str(palavra)] = 1
        else:
            return 2
            dicionario[palavra] += 1
    return dicionario