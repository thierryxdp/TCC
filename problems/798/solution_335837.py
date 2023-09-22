def freq_palavras(frases):
    """Funcao que recebe uma string e retorna um dicionario onde cada palavra dessa string e uma chave e o valor seja quantas vezes a palavra aparece. str=>dict"""
    dicionario={}
    totaldepalavras= str.split(frases)
    for palavra in totaldepalavras:
        dicionario[palavra]=list.count(totaldepalavras)
    return dicionario