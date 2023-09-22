def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionário onde cada palavra
    dessa string é uma chave e tem como valor o número de vezes
    que a palavra aparece
    str->dic'''
    frase= str.split(frases)
    frequencia={}
    for palavra in frase:
        quantidade=list.count(frase,palavra)
        frequencia[palavra]=quantidade
    return palavra